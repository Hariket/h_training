from odoo import api, fields, models


class StockMoveKsc(models.Model):
    _name = 'stock.move.ksc'

    name = fields.Char(string='Name')
    product_id = fields.Many2one('product.ksc', required=True)
    uom_id = fields.Many2one('product.uom.ksc', required=True)
    source_location_id = fields.Many2one('stock.location.ksc')
    destination_location_id = fields.Many2one('stock.location.ksc')
    qty_to_deliver = fields.Float('Qty To Deliver')
    qty_delivered = fields.Float('Qty Delivered')
    state = fields.Selection([('draft', 'Draft'), ('done', 'Done'), ('cancelled', 'Cancelled')],
                             string='State')
    sale_line_id = fields.Many2one('sale.order.line.ksc')
    purchase_line_id = fields.Many2one('purchase.order.line.ksc')
    stock_inventory_id = fields.Many2one('stock.inventory.ksc')
    picking_id = fields.Many2one('stock.picking.ksc')
    order_line_id = fields.Many2one('sale.order.line.ksc')

