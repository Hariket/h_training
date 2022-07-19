# -*- coding: utf-8 -*-

{
    'name': 'Product Ksc',
    'version': '15.0.2.1.0',
    'description': """Helps to manage product architecture for the organisation""",
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/product_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
