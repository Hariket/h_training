# -*- coding: utf-8 -*-

{
    'name': 'Crm Lead Ksc',
    'version': '15.3.2.1.1',
    'summary': 'Crm lead',
    'description': """Helps to manage lead architecture for the organisation""",
    'category': 'CRM',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/lead_views.xml',
        'security/crm_lead_ksc_security.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
