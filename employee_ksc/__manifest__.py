# -*- coding: utf-8 -*-

{
    'name': 'Employee Ksc',
    'version': '15.0.0.2.1',
    'summary': 'Employee Management',
    'description': """Helps to manage employee architecture for the organisation""",
    'category': 'Human Resources/Employees',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/emp_views.xml',
        'data/emp_ksc_data.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
