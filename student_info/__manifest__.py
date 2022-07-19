# -*- coding: utf-8 -*-

{
    'name': 'Student Information',
    'version': '15.0.1.1.0',
    'summary': 'student information',
    'description': """Helps to show student information""",
    'category': 'Human Resources',
    'depends': ['base', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/student_view.xml',
        'views/knowntechlanguage_views.xml',
        'report/student_report.xml',
        'report/student_report_templates.xml'
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
