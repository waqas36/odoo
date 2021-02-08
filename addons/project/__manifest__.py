# -*- coding: utf-8 -*-
# Part of PureDigital. See LICENSE file for full copyright and licensing details.

{
    'name': 'Project',
    'version': '1.1',
    'website': 'https://www.puredigital.co.nz/page/project-management',
    'category': 'Services/Project',
    'sequence': 45,
    'summary': 'Organize and plan your projects',
    'depends': [
        'analytic',
        'base_setup',
        'mail',
        'portal',
        'rating',
        'resource',
        'web',
        'web_tour',
        'digest',
    ],
    'description': "",
    'data': [
        'security/project_security.xml',
        'security/ir.model.access.csv',
        'data/digest_data.xml',
        'report/project_report_views.xml',
        'views/analytic_views.xml',
        'views/digest_views.xml',
        'views/rating_views.xml',
        'views/project_views.xml',
        'views/res_partner_views.xml',
        'views/res_config_settings_views.xml',
        'views/mail_activity_views.xml',
        'views/project_assets.xml',
        'views/project_portal_templates.xml',
        'data/digest_data.xml',
        'data/project_mail_template_data.xml',
        'data/project_data.xml',
        'wizard/project_delete_wizard_views.xml',
        'wizard/project_task_type_delete_views.xml',
    ],
    'demo': ['data/project_demo.xml'],
    'qweb': ['static/src/xml/project_templates.xml'],
    'test': [
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}