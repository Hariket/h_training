# -*- coding: utf-8 -*-

{
    'name': 'Localization Management',
    'version': '15.3.0.1.0',
    'summary': 'Localization Management',
    'description': """Helps to manage location architecture """,
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/country_views.xml',
        'views/state_views.xml',
        'views/city_views.xml',
        'report/localization_report.xml',
        'report/localization_report_templates.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
