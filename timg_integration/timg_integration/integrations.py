from __future__ import unicode_literals
import frappe
import requests
import json

def send_email_notification(doc, method=None):
    integration_settings = frappe.get_single("TIMG Integration Settings")
    if integration_settings.get('email_notification_enabled') == 1:
        emails = []
        for email_setting in integration_settings.get('emails'):
            if email_setting.is_active == 1:
                emails.append(email_setting.email)
        if emails:
            subject = "{0} {1} was removed".format(doc.doctype, doc.name)
            message = "This message was sent automatically to inform you that {0} {1} was removed".format(doc.doctype, doc.name)
            try:
                frappe.sendmail(recipients=emails, subject=subject, message=message, delayed=False)
            except:
                frappe.msgprint("Missing Email config")
            else:
                frappe.msgprint("Email Notification sent successfully")

def get_jwt_token(url, username, password):
    data = '''mutation {
                tokenCreate(email: "''' + username + '''", password: "''' + password + '''") {
                    token
                    user {
                        email
                    }
                    errors {
                        field
                        message
                    }
                }
            }'''
    request = requests.post(url, json={'query': data})
    response = json.loads(request.text)
    if response["data"]["tokenCreate"]:
        return response["data"]["tokenCreate"]["token"]
    else:
        return None

def send_item_information(doc, method=None):
    integration_settings = frappe.get_single("TIMG Integration Settings")
    if integration_settings.get('saleor_integration_enabled') == 1:
        url = integration_settings.get('saleor_integration_url')
        username = integration_settings.get('saleor_integration_username')
        password = integration_settings.get_password(fieldname="saleor_integration_password", raise_exception=False)
        token = get_jwt_token(url, username, password)
        if token:
            header = {
                "Content-type": "application/json",
                "Authorization": "JWT " + token
            }
            data = '''mutation{
                productCreate(input:{productType:"UHJvZHVjdFR5cGU6MTE=",name:"''' + doc.item_code + '''",description:"''' + doc.description + ''''",basePrice: ''' + str(doc.standard_rate) + '''}){
                    errors{
                        field
                        message
                    }
                    product{
                        id
                        name
                    }
                }
            }'''
            request = requests.post(url, headers=header, json={'query': data})
            response = json.loads(request.text)
            if response['errors']:
                frappe.throw(response['errors'][0]['message'])
            else:
                frappe.msgprint("Item {0} created successfully".format(response['data']['productCreate']['id']))
        else:
            frappe.throw("Error while authenticating")