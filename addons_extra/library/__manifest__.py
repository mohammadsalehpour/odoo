# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Library',
    'version': '1.0.0',
    'category': 'DameDast',
    'sequence': 30,
    'summary': 'Software from DameDast',
    'author': "Mohammad Salehpour",
    'description': "",
    'website': 'https://damedast.com',
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/book_view.xml',
        'views/author_view.xml',
        'views/borrower_book_view.xml',
        'views/borrower_view.xml',
        'views/menus_view.xml',
    ],
}
