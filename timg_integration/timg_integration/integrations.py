from __future__ import unicode_literals
import frappe

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
