# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "timg_integration"
app_title = "Timg Integration"
app_publisher = "seethersan"
app_description = "App for Integration with TIMG systems"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "carlos_jcez@hotmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/timg_integration/css/timg_integration.css"
# app_include_js = "/assets/timg_integration/js/timg_integration.js"

# include js, css files in header of web template
# web_include_css = "/assets/timg_integration/css/timg_integration.css"
# web_include_js = "/assets/timg_integration/js/timg_integration.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "timg_integration.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "timg_integration.install.before_install"
# after_install = "timg_integration.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "timg_integration.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Customer": {
		"on_trash": "timg_integration.timg_integration.integrations.send_email_notification"
	},
    "Item": {
        "on_trash": "timg_integration.timg_integration.integrations.send_email_notification",
        "before_insert": "timg_integration.timg_integration.integrations.send_item_information",
    }
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"timg_integration.tasks.all"
# 	],
# 	"daily": [
# 		"timg_integration.tasks.daily"
# 	],
# 	"hourly": [
# 		"timg_integration.tasks.hourly"
# 	],
# 	"weekly": [
# 		"timg_integration.tasks.weekly"
# 	]
# 	"monthly": [
# 		"timg_integration.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "timg_integration.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "timg_integration.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "timg_integration.task.get_dashboard_data"
# }

