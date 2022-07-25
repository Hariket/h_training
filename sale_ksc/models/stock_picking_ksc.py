from odoo import api, fields, models
from datetime import datetime


class StockPickingKsc(models.Model):
    _name = 'stock.picking.ksc'
    _description = 'Stock Picking'

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

    @api.depends('move_ids', 'stock_move_count')
    def _compute_stock_move_count(self):
        for rec in self:
            rec.stock_move_count = len(rec.move_ids.ids)

    def action_view_moving(self):
        '''
            This function returns an action that displays the opportunities from partner.
        '''
        action = self.env["ir.actions.actions"]._for_xml_id("sale_ksc.action_stock_move_ksc")
        action['domain'] = [('id', 'in', self.move_ids.ids)]
        move = self.move_ids
        if len(move) == 1:
            action['views'] = [(self.env.ref('sale_ksc.form_view_stock_move_ksc').id, 'form')]
            action['res_id'] = move.id
        return action
