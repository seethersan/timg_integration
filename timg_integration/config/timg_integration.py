from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
        {
            "label": _("Configuración"),
            "items": [
                {
                    "type": "doctype",
                    "name": "TIMG Integration Settings",
					"onboard": 1,
                }
            ]
        }
    ]