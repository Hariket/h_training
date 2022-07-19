from odoo import api, fields, models


class Product(models.Model):
    _inherit = "product.product"

    deposit_product_id = fields.Many2one('product.product')
    deposit_product_qty = fields.Integer(string='Deposit Product qty')
    profit = fields.Float(string='Profit', compute='_compute_profit_order')

    def _compute_profit_order(self):
        self.profit = self.standard_price - self.lst_price
