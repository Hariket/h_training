# -*- coding: utf-8 -*-

{
    'name': 'Sale Management',
    'version': '15.2.1',
    'summary': 'Sale Management',
    'description': """Helps to manage sale architecture for the organisation""",
    'category': 'Human Resources/Employees',
    'depends': ['base', 'sale_ksc', 'sale', 'crm', 'purchase'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/sale_salesperson_info_views.xml',
        'data/sale_order_extended_data.xml',
        'views/sale_order_views.xml',
        'views/product_views.xml',
        'views/purchase_order_views.xml',
        'views/stock_move_line_views.xml',
        'report/sale_report.xml',
        'report/sale_report_templates.xml',
        'report/saleperson_report.xml',
        'report/saleperson_report_templates.xml',
        'report/product_picking.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
