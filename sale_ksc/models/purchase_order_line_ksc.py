from odoo import api, fields, models


class PurchaseOrderLineKsc(models.Model):
    _name = 'purchase.order.line.ksc'
    _description = 'Purchase Order Lines'

    order_no_id = fields.Many2one('purchase.order.ksc')
    product_id = fields.Many2one('product.ksc')
    name = fields.Text(string='Description')
    quantity = fields.Float(digits=(6, 2))
    unit_price = fields.Float(digits=(6, 2))
    state = fields.Selection(
        [('draft', 'Draft'), ('confirmed', 'Confirmed'), ('done', 'Done'), ('cancelled', 'Cancelled')])
    uom_id = fields.Many2one('product.uom.ksc')

    subtotal = fields.Float(compute='_compute_subtotal', store=True)

    @api.onchange('product_id')
    def _onchange_product(self):
        if self.product_id:
            self.unit_price = self.product_id.sale_price
            self.quantity = 1

    @api.depends('quantity', 'unit_price')
    def _compute_subtotal(self):
        '''
        it calculate the subtotal
        :return: True
        '''
        self.subtotal = self.quantity * self.unit_price
