from odoo import api, fields, models


class ProductKsc(models.Model):
    _name = 'product.ksc'

    name = fields.Char(string='Name Of The Product', required=True)
    sku = fields.Char(string='Stock Keeping Unit')
    weight = fields.Float('weight')
    length = fields.Float('length')
    volume = fields.Float('volume')
    width = fields.Float('width')
    barcode = fields.Char(String='Barcode')
    product_type = fields.Selection([('storable', 'Storable'), ('consumable', 'Consumable'),
                                     ('service', 'Service')], string='Product Type')
    sale_price = fields.Float('sale_price', default=1.00)
    cost_price = fields.Float('cost_price', default=1.00)
    product_category = fields.Many2one('product.category.ksc', string='Product Category')
    uom = fields.Many2one('product.uom.ksc', string='Unit Of Measure')
    tax_ids = fields.Many2many('account.tax.ksc')

    def update_stock_object_type(self):
        return {
            'name': ('Product Stock Update'),
            'view_mode': 'form',
            'res_model': 'product.stock.update.ksc',
            'view_id': False,
            'type': 'ir.actions.act_window',
            'target': 'new',
        }
