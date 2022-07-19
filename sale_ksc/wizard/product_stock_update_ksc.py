from odoo import api, fields, models


class ProductStockUpdateKsc(models.TransientModel):
    _name = 'product.stock.update.ksc'

    location_id = fields.Many2one('stock.location.ksc')
    current_stock = fields.Float('Current Stock')
    counted_qty = fields.Float('Counted Qty')
    difference_qty = fields.Float('Difference Qty', compute='_compute_counted_stock_difference',
                                  store=False)

    def _compute_counted_stock_difference(self):
        for product in self:
            product.difference_qty = product.counted_qty - product.current_stock

    def update_stock(self):
        pass
