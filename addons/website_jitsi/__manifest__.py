# -*- coding: utf-8 -*-
# Part of PureDigital. See LICENSE file for full copyright and licensing details.


{
    "name": "Website Jitsi",
    'category': 'Hidden',
    'version': '1.0',
    "summary": "Create Jitsi room on website.",
    'website': 'https://www.puredigital.co.nz/page/events',
    "description": "Create Jitsi room on website.",
    "depends": [
        "website"
    ],
    "data": [
        'views/assets.xml',
        'views/chat_room_templates.xml',
        'views/chat_room_views.xml',
        'views/res_config_settings.xml',
        'security/ir.model.access.csv',
    ],
    'application': False,
}
