from odoo import fields, models, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    profit_margin = fields.Float(compute='_compute_profit')
    profit_value = fields.Float(compute='_compute_profit')
    custom_warehouse_id = fields.Many2one('stock.warehouse', readonly=False)
    history_unit_price = fields.Float()

    @api.onchange('product_uom_qty')
    def onchange_product_uom_qty_change_deposit_p_qty(self):
        product = self.order_id.order_line.filtered(
            lambda x: x.product_id == self.product_id.deposit_product_id
        )
        if product:
            product._origin.update({
                'product_uom_qty': product.product_id.product_deposit_qty * self.product_uom_qty
            })

    def _compute_profit(self):
        for line in self:
            line.profit_value = 0
            line.profit_margin = 0

            profit_value = line.price_unit - line.product_id.standard_price
            if line.product_uom_qty:
                line.profit_value = line.product_uom_qty * profit_value
                if line.price_unit:
                    line.profit_margin = (profit_value / line.price_unit) * 100
            else:
                line.profit_value = profit_value
                if line.price_unit:
                    line.profit_margin = (profit_value / line.price_unit) * 100

    def _prepare_procurement_values(self, group_id=False):
        values = super(SaleOrderLine, self)._prepare_procurement_values(group_id)
        values.update({
            'warehouse_id': self.custom_warehouse_id if self.custom_warehouse_id else self.order_id.warehouse_id
        })
        return values

    @api.onchange('product_id')
    def onchange_product(self):
        last_rec = self.env['sale.order'].search(
                        [('state', '=', 'sale'), ('partner_id', '=', self.order_id.partner_id.id)], order='id desc', limit=1)
        if last_rec:
            for line in last_rec.order_line:
                if self.product_id.id == line.product_id.id:
                    self.history_unit_price = line.price_unit
        else:
            self.history_unit_price = 0
        # customer_recs = self.env['sale.order'].search([])
        # for customer in customer_recs:
        #     if self.partner_id.id == customer.partner_id.id:
        #         last_rec = \
        #             self.env['sale.order'].search(
        #                 [('state', '=', 'sale'), ('partner_id', '=', self.order_id.partner_id.id)], order='id desc')[0]
        #         for line in last_rec.order_line:
        #             if line.product_id.id == self.product_id.id:
        #                 self.history_unit_price = line.price_unit
        #     else:
        #         self.history_unit_price = 0
        #         pass

