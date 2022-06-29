# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Store',
    'version': '1.0.0',
    'category': 'DameDast/Store',
    'sequence': 20,
    'summary': 'Software from DameDast',
    'author': "Mohammad Salehpour",
    'description': "",
    'website': 'https://damedast.com',
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'data': [
        'security/store_security.xml',
        'security/ir.model.access.csv',
        'views/store_view.xml',
        'views/product_view.xml',
        'views/menus_view.xml',
    ],
}
