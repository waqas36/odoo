# -*- coding: utf-8 -*-
# Part of PureDigital. See LICENSE file for full copyright and licensing details.

{
    'name': 'Italy - E-invoicing',
    'version': '0.3',
    'depends': [
        'l10n_it',
        'fetchmail',
        'account_edi'
    ],
    'author': 'PureDigital',
    'description': """
E-invoice implementation
    """,
    'category': 'Accounting/Localizations/EDI',
    'website': 'http://www.puredigital.co.nz/',
    'data': [
        'security/ir.model.access.csv',
        'data/account_edi_data.xml',
        'data/invoice_it_template.xml',
        'views/l10n_it_view.xml',
        ],
    'demo': [
        'data/account_invoice_demo.xml',
    ],
    'auto_install': True,
}
