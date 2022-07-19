# -*- coding: utf-8 -*-

{
    'name': 'Student Information Extended',
    'version': '15.0.4.1.0',
    'category': 'Human Resources/Employees',
    'depends': ['student_info', 'portal', 'mail', 'utm'],
    'data': [
        'views/student_views.xml',
        'report/student_report_inherit_templates.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
