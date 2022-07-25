from odoo import api, fields, models


class StockMoveLine(models.Model):
    _inherit = 'stock.move'

    sku = fields.Integer(string='Stock Keeping Unit')
