# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'University',
    'version': '1.0.0',
    'category': 'DameDast/University',
    'sequence': 10,
    'summary': 'Software from DameDast',
    'author': "Mohammad Salehpour",
    'description': "",
    'website': 'https://damedast.com',
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    'data': [
        'security/university_security.xml',
        'security/ir.model.access.csv',
        'views/university_view.xml',
        'views/student_view.xml',
        'views/menus_view.xml',
    ],
}
