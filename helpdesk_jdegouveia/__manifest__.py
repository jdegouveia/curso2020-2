# Copyright 2021 Jdegouveia
# Jdegouveia jdegouvei@ticomsa.com
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    "name": "Helpdesk Jdegouveia",
    "summary": "Helpdesk And Tickets",
    "version": "13.0.1.0.0",
    "category": "Helpdesk",
    "website": "https://github.com/OCA/helpdesk",
    "author": "Jdegouveia, Odoo Community Association (OCA)",
    "maintainers": ["jdegouveia"],
    "license": "AGPL-3",
    "application": True,
    "installable": True,
    "depends": [
        "base",
    ],
    "data": [
        "security/helpdesk_security.xml",
        "security/ir.model.access.csv",
        "views/helpdesk_ticket_views.xml",
        "views/helpdesk_tag_views.xml",
    ],
    "demo": [
    ]
}
