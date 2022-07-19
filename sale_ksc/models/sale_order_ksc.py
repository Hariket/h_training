from odoo import api, fields, models
from datetime import date


class SaleOrderKsc(models.Model):
    _name = 'sale.order.ksc'

    name = fields.Char(string='Order Name', required=True)
    crm_lead_id = fields.Many2one('lead.ksc', readonly=True)
    customer_id = fields.Many2one('res.partner.ksc')
    invoice_customer = fields.Many2one('res.partner.ksc')
    shipping_customer = fields.Many2one('res.partner.ksc')
    sale_order_date = fields.Date(string='Sale Order Date')
    order_line_ids = fields.One2many(comodel_name='sale.order.line.ksc',
                                     inverse_name='order_no')
    salesperson = fields.Many2one('res.users')
    state = fields.Selection([('draft', 'Draft'), ('confirmed', 'Confirmed'),
                              ('done', 'Done'), ('cancelled', 'Cancelled')], string='State')
    total_weight = fields.Float(string='Total Weight', compute='compute_weight',
                                digits=(10, 2), store=False)
    total_volume = fields.Float(string='Total Volume', compute='compute_volume',
                                digits=(10, 2), store=False)
    order_total = fields.Float(string='Order Total', compute='_compute_ordertotal', store=True)
    lead_id = fields.Many2one('lead.ksc')
    warehouse_id = fields.Many2one('stock.warehouse.ksc')
    picking_ids = fields.One2many(comodel_name='stock.picking.ksc',
                                  inverse_name='order_id', readonly=True)
    amount_untaxed = fields.Float(compute='_compute_untaxed_amount')
    total_tax = fields.Float(compute='_compute_total_tax', store=True)
    total_amount = fields.Float(compute='_compute_total_amount', store=True)

    @api.depends('order_line_ids')
    def compute_weight(self):
        total_weights = []
        self.total_weight = 0
        for rec in self.order_line_ids:
            total_w = rec.quantity * rec.product.weight
            if total_w:
                total_weights.append(total_w)

        self.total_weight = sum(total_weights)

    @api.depends('order_line_ids')
    def compute_volume(self):
        for rec in self:
            rec.total_volume = sum(rec.order_line_ids.mapped('product').mapped('volume'))

    @api.depends('order_total')
    def _compute_ordertotal(self):
        for rec in self:
            rec.order_total = sum(rec.order_line_ids.mapped('subtotal_without_tax'))

    @api.onchange('customer_id')
    def onchange_load_shipping_invoice_address(self):
        shipping_customers = self.customer_id.child_ids.filtered(lambda c: c.address_type == 'shipping')
        self.shipping_customer = shipping_customers[0] if shipping_customers else False

        invoice_customers = self.customer_id.child_ids.filtered(lambda c: c.address_type == 'invoice')
        self.invoice_customer = invoice_customers[0] if invoice_customers else False

    @api.depends('order_line_ids')
    def _compute_total_tax(self):
        for order in self:
            order.total_tax = 0
            for line in order.order_line_ids:
                order.total_tax += line.subtotal_tax

    @api.depends('order_line_ids')
    def _compute_untaxed_amount(self):
        for order in self:
            order.amount_untaxed = 0
            for line in order.order_line_ids:
                order.amount_untaxed += line.subtotal_tax

    @api.depends('order_line_ids')
    def _compute_total_amount(self):
        for order in self:
            order.total_amount = order.amount_untaxed + order.total_tax
