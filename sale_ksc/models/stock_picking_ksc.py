from odoo import api, fields, models
from datetime import datetime


class StockPickingKsc(models.Model):
    _name = 'stock.picking.ksc'

    name = fields.Char(string='Name', index=True)
    partner_id = fields.Many2one('res.partner.ksc')
    back_order_id = fields.Many2one('stock.picking.ksc')
    state = fields.Selection([('draft', 'Draft'), ('validate', 'Validate'),
                              ('cancelled', 'Cancelled')], string='State', default='draft')
    sale_order_id = fields.Many2one('sale.order.ksc')
    purchase_order_id = fields.Many2one('purchase.order.ksc')
    transaction_type = fields.Selection([('in', 'In'), ('out', 'Out')], string='Transaction Type')
    move_ids = fields.One2many(comodel_name='stock.move.ksc',
                               inverse_name='picking_id')
    transaction_date = fields.Date('Date', default=datetime.today())
    parent_picking_id = fields.Many2one('stock.picking.ksc')
    order_id = fields.Many2one('sale.order.ksc')
