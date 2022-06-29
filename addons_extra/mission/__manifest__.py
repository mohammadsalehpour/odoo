# -*- coding: utf-8 -*-

{
    'name': 'Mission',
    'summary': 'Mission',
    'descreption': '...',
    'sequence': 0,
    'author': '...',
    'company': 'GEG',
    'website': '...',
    'category': 'HR',
    'version': '14.1',

    'depends': ['base', 'hr', 'contacts'],

    'data':['security/mission_security.xml',
            'security/ir.model.access.csv',
            'views/mission_views.xml',
            'views/cost_percentage_views.xml',
            'views/travel_ticket_views.xml',
            'views/accomodation_views.xml',
            'views/hr_employee_views.xml',
            'views/res_partner_views.xml',
            'views/menus.xml',], 
    'application': False,
    'installable': True,
    'auto_install': False,

}