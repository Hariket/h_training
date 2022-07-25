from odoo import api, fields, models
from datetime import datetime


class StockInventoryKsc(models.Model):
    _name = 'stock.inventory.ksc'
    _description = 'Stock Inventory'

    name = fields.Char(string='Name')
    state = fields.Selection([('draft', 'Draft'), ('in-progress', 'In Progress'), ('done', 'Done'),
                              ('cancelled', 'Cancelled')], string='State')
    location_id = fields.Many2one('stock.location.ksc')
    inventory_date = fields.Date('Date', default=datetime.today())
    inventory_line_ids = fields.One2many(comodel_name='stock.inventory.line.ksc',
                                         inverse_name='stock_inventory_id')

    def action_start_inventory(self):
        self.state = 'in_progress'
        if self.inventory_line_ids:
            for each_product in self.inventory_line_ids:
                each_product.available_qty = each_product.product_id.with_context(
                    {'get_location': self.location_id.id}).product_qty
