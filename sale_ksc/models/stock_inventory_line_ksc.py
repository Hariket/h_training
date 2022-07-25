from odoo import api, fields, models


class StockInventoryLineKsc(models.Model):
    _name = 'stock.inventory.line.ksc'
    _description = 'Stock Inventory Lines'

    name = fields.Char(string='Name')
    product_id = fields.Many2one('product.ksc')
    stock_inventory_id = fields.Many2one('stock.inventory.ksc')
    available_qty = fields.Float('Available Qty')
    counted_product_qty = fields.Float('Counted Product Qty')
    difference = fields.Float(string='Difference', compute='_compute_difference')

    def _compute_difference(self):
        '''
        this compute field is find the difference between counted product quantity and available quantity
        :return: True
        '''
        for line in self:
            line.difference = \
                line.counted_product_qty - line.available_qty
