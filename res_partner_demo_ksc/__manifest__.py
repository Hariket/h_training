# -*- coding: utf-8 -*-

{
    'name': 'Res Partner Management',
    'version': '15.0.1.1.2',
    'summary': 'Management',
    'description': """Helps to manage partner architecture for the organisation""",
    'category': 'Human Resources/Employees',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/partner_views.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
