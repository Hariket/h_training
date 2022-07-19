from odoo import models, fields, api


class Product(models.Model):
    _inherit = "product.product"

    deposit_product_id = fields.Many2one('product.product')
    product_deposit_qty = fields.Integer()

