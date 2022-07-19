from odoo import models, fields, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    profit_margin = fields.Float(string='Margin', digits='Product Price', store=True,
                                 compute='_compute_profit')
    profit_value = fields.Float(compute='_compute_profit')
    warehouse_id = fields.Many2one('stock.warehouse', readonly=False, store=True)
    history_unit_price = fields.Float(string='History Unit Price')

    def _compute_profit(self):
        for line in self:
            line.profit_value = 0
            line.profit_margin = 0

            profit_value = line.price_unit - line.product_id.standard_price
            if line.product_id.standard_price != 0:
                line.profit_value = line.product_uom_qty * profit_value
                if line.price_unit:
                    line.profit_margin = (profit_value * 100) / line.product_id.standard_price
            else:
                line.profit_margin = 0

    def _prepare_procurement_values(self, group_id=False):
        values = super(SaleOrderLine, self)._prepare_procurement_values(group_id)
        values.update(
            {
                'warehouse_id':
                    self.warehouse_id
                    if self.warehouse_id
                    else self.order_id.warehouse_id
            })
        return values

    @api.onchange('product_id')
    def onchange_product(self):
        last_rec = self.env['sale.order'].search(
            [('state', '=', 'sale'), ('partner_id', '=', self.order_id.partner_id.id)], order='id desc',
            limit=1)
        if last_rec:
            for line in last_rec.order_line:
                if self.product_id.id == line.product_id.id:
                    self.history_unit_price = line.price_unit
        else:
            self.history_unit_price = 0

    def _prepare_procurement_values(self, group_id=False):
        values = super(SaleOrderLine, self)._prepare_procurement_values(group_id)
        values.update(
            {
                'warehouse_id':
                    self.warehouse_id
                    if self.warehouse_id
                    else self.order_id.warehouse_id
            })
        return values
