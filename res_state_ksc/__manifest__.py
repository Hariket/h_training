# -*- coding: utf-8 -*-

{
    'name': 'Res State Management',
    'version': '15.0.1.1.3',
    'summary': 'Management',
    'description': """Helps to manage state architecture for the organisation""",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/state_views.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
