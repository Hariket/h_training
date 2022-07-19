# -*- coding: utf-8 -*-

{
    'name': 'Res city Management',
    'version': '15.0.1.2.3',
    'summary': 'Management',
    'description': """Helps to manage city architecture for the organisation""",
    'category': '',

    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/city_views.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
