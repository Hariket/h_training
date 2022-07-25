# -*- coding: utf-8 -*-

{
    'name': 'Res Country Management',
    'version': '15.0.1.1.2',
    'summary': 'Management',
    'description': """Helps to manage country architecture for the organisation""",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/country_views.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
