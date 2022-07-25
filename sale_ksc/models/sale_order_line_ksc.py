from odoo import api, fields, models


class SaleOrderLineKsc(models.Model):
    _name = 'sale.order.line.ksc'
    _description = 'Sale Order Lines'

    order_no = fields.Many2one('sale.order.ksc')
    product = fields.Many2one('product.ksc')
    name = fields.Text(string='Description')
    quantity = fields.Float('Quantity', digits=(6, 2))
    unit_price = fields.Float('Unit Price', digits=(6, 2))
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'),
                              ('cancelled', 'Cancelled')], string='State')
    uom_id = fields.Many2one('product.uom.ksc')
    subtotal_without_tax = fields.Float(compute='compute_withouttax', string='Subtotal Without Tax')
    stock_move_ids = fields.One2many(comodel_name='stock.move.ksc',
                                     inverse_name='order_line_id')
    delivered_qty = fields.Float(compute='_compute_delivered_qty')
    warehouse_id = fields.Many2one('stock.warehouse.ksc')
    subtotal_tax = fields.Float(compute='compute_subtotal_tax', store=True)

    @api.onchange('product')
    def _onchange_product(self):
        for record in self:
            if record.product.sale_price:
                record.unit_price = record.product.sale_price
            else:
                record.unit_price = 0
                record.quantity = 1

    @api.depends('quantity', 'unit_price')
    def compute_withouttax(self):
        '''
        this field is depended on quantity and unit price and this field calculate the subtotal without tax
        '''
        for rec in self:
            rec.subtotal_without_tax = rec.quantity * rec.unit_price

    def _compute_delivered_qty(self):
        '''
        when the stock move is in the done state then it move into delivered quantity
        '''
        for line in self:
            delivered_qty = 0
            for stock_move in self.stock_move_ids.filtered(lambda c: c.state == 'done'):
                delivered_qty += stock_move.qty_delivered
            line.delivered_qty = delivered_qty

    @api.depends('quantity', 'unit_price')
    def compute_subtotal_tax(self):
        '''
        this field is depended on quantity and unit price and it calculate subtotal tax
        '''
        for rec in self:
            rec.subtotal_tax = rec.quantity * rec.unit_price
