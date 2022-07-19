from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class PurchaseOrderKsc(models.Model):
    _name = 'purchase.order.ksc'

    name = fields.Char(string='Name')
    order_number = fields.Char()
    partner_id = fields.Many2one('res.partner.ksc', string='Vendor', required=True)
    vendor_reference = fields.Char()
    order_deadline = fields.Date()
    receipt_date = fields.Date()
    purchase_line_ids = fields.One2many('purchase.order.line.ksc', 'order_no_id')
    state = fields.Selection(
        [('draft', 'Draft'), ('confirmed', 'Confirmed'), ('done', 'Done'),
         ('cancelled', 'Cancelled')])
    total_weight = fields.Float(compute='_compute_total_weight', store=True)
    order_total = fields.Float(compute='_compute_order_total', store=True)
    warehouse_id = fields.Many2one('stock.warehouse.ksc')

    def action_confirm_order(self):
        self.state = 'confirmed'
        if not self.partner_id:
            raise ValidationError(_('Create Customer First'))
        else:
            picking = self.env['stock.picking.ksc'].create({
                'partner_id': self.partner_id.id,
                'purchase_order_id': self.id,
                'transaction_type': 'in',
            })

            # print("\n\nDDDDDDDDDDDDD", self)
            # print("\n\nLIne>>>>>>>>>>", self.purchase_line_ids)
            # self.env['stock.move.ksc'].create({
            #     'destination_location_id': self.warehouse_id.stock_location_id.id,
            # })

            for rec in self.purchase_line_ids:
                self.env['stock.move.ksc'].create({
                    'product_id': rec.product_id.id,
                    'uom_id': rec.uom_id.id,
                    'qty_to_deliver': rec.quantity,
                    'purchase_line_id': rec.id,
                    'source_location_id': self.env['stock.location.ksc'].search([('location_type', '=', 'vendor')],
                                                                                limit=1).id,
                    'picking_id': picking.id,
                    'destination_location_id': rec.order_no_id.warehouse_id.stock_location_id.id,

                })

    @api.depends('purchase_line_ids.product_id')
    def _compute_total_weight(self):
        for rec in self:
            if rec.purchase_line_ids:
                sum_weight = 0
                for records in rec.purchase_line_ids:
                    sum_weight += records.product_id.weight
                rec.total_weight = sum_weight

    @api.depends('purchase_line_ids.subtotal')
    def _compute_order_total(self):
        for rec in self:
            if rec.purchase_line_ids:
                subtotal_sum = 0
                for records in rec.purchase_line_ids:
                    subtotal_sum += records.subtotal
                rec.order_total = subtotal_sum
