from odoo import api, fields, models


class ProductCategoryKsc(models.Model):
    _name = 'product.category.ksc'
    _description = 'Product Category'

    name = fields.Char(string='Name Of Category')
    parent_id = fields.Many2one('product.category.ksc', String='Parent Id')
