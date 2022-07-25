from odoo import api, fields, models


class ProductKsc(models.Model):
    _name = 'product.ksc1'
    _description = 'Product'

    name = fields.Char(string='Name of the Product', copy=False)
    sku = fields.Char(string='SKU(Stock Keeping Unit) of the Product', copy=False)
    barcode = fields.Char(string='Barcode of the Product', copy=False)
    can_this_product_be_sold = fields.Boolean('Sold')
    product_type = fields.Selection([('storable', 'Storable'), ('consumable', 'Consumable'),
                                     ('service', 'Service')], string='Product Type')
    sale_price = fields.Float('Sale Price', digits=(6, 2))
    cost_price = fields.Float('Cost Price', digits=(6, 2))
    active = fields.Boolean('Active')
    warehouse = fields.Char(string='Warehouse', copy='False')
    product_image = fields.Image('Product Image')
    website_description = fields.Html('Website Description')
    internal_note = fields.Text('Internal Note')




