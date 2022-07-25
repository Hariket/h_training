from odoo import api, fields, models


class ProductUomKsc(models.Model):
    _name = 'product.uom.ksc'
    _description = 'Product Uom'

    name = fields.Char(string='Name Of The Stock Keeping Unit')
    uom_category = fields.Many2one('product.uom.category.ksc')
