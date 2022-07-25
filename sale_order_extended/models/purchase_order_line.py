from odoo import models, fields, api


class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    history_unit_price = fields.Float(string='History Unit Price')

    @api.onchange('product_id')
    def onchange_product(self):

        last_rec = self.env['purchase.order'].search(
            [('state', '=', 'purchase'), ('partner_id', '=', self.order_id.partner_id.id)], order='id desc',
            limit=1)
        if last_rec:
            for line in last_rec.order_line:
                if self.product_id.id == line.product_id.id:
                    self.history_unit_price = line.price_unit
