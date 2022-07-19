# -*- coding: utf-8 -*-

{
    'name': 'Konsultoo Employee Management',
    'version': '15.0.0.1.0',
    'summary': 'Employee Management',
    'description': """Helps to manage employee architecture for the organisation""",
    'category': 'Human Resources/Employees',
    'website': 'https://www.konsultoo.com/',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/employee_views1.xml',
        'views/employee_position_views.xml',
        'views/knowntechlang_views.xml',
        'views/employee_hobbies_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
