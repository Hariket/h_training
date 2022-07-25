from odoo import api, fields, models


class ProductUomCategoryKsc(models.Model):
    _name = 'product.uom.category.ksc'
    _description = 'Product Uom Category'

    name = fields.Char(string='Name UOM Category')
    uom_ids = fields.One2many(comodel_name='product.uom.ksc',
                              inverse_name='uom_category', string='UOM Ids')
