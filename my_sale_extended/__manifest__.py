{
    'name': 'My Sale Extended',
    'depends': ['sale_crm'],
    'data' : [
        'security/ir.model.access.csv',
        'data/data_crm_tag_ids.xml',
        'data/data_product.xml',
        'views/sale_order_view.xml',
        'views/project_tag_view.xml',
        'reports/groupby_product_picking.xml',
        'reports/salesperson_orders_detail_template.xml',
        'reports/reports.xml',
        'wizard/sales_person_view.xml'
    ],
    'installable': True,
    'auto_install': False,
}
