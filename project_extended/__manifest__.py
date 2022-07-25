# -*- coding: utf-8 -*-

{
    'name': 'Project Management',
    'version': '15.2.1',
    'summary': 'Project Management',
    'description': """Helps to manage project architecture for the organisation""",
    'category': 'Services',
    'depends': ['base', 'project'],
    'data': [
        'views/project_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
