# -*- coding: utf-8 -*-

{
    'name': 'Employee Management Konsultoo',
    'version': '15.4.0.1.0',
    'summary': 'Employee Management',
    'description': """Helps to manage employee architecture for the organisation""",
    'category': 'Human Resources/Employees',
    'website': 'https://www.konsultoo.com/',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/department_views.xml',
        'views/department_shift_views.xml',
        'views/employee_ksc_views.xml',
        'views/employee_leave_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
