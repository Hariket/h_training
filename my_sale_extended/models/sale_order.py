from odoo import models, fields, api
from odoo.tests import tagged, Form


class SaleOrder(models.Model):
    _inherit = "sale.order"

    custom_opportunity_crm_lead_id = fields.Many2one('crm.lead', string='Opportunity')
    custom_opportunity_tag_ids = fields.Many2many('crm.tag', string='Tags')
    product_tmpl_ids = fields.Many2many('product.template')
    is_all_picking_completed = fields.Boolean(compute='_compute_if_delivery_orders_completed')

    def action_confirm(self):
        rec = self.env.ref('my_sale_extended.data_product_product_shipping_charge')
        if not self.order_line.filtered('is_delivery'):
            self.write({'order_line': [(0, 0, {
                'product_id': rec.id,
                'price_unit': rec.list_price,
                'product_uom_qty': 1,
                'is_delivery': True})]})

        return super(SaleOrder, self).action_confirm()

    def manage_deposit(self):
        deposit_products_ids = self.order_line.mapped('product_id.deposit_product_id').filtered(
            lambda x: x not in self.order_line.mapped('product_id')
        )

        if deposit_products_ids:
            for product in deposit_products_ids:
                self.write({
                    'order_line': [(0, 0, {
                        'product_id': product.id,
                        'name': product.name,
                        'product_uom_qty': product.product_deposit_qty,
                        'price_unit': product.list_price
                    })]
                })

    def scan_all_sale_order_line(self):
        records = self.search(['|', '|', ('id', '=', self.id), ('state', '!=', 'done'), ('state', '!=', 'cancel')])
        lines = records.order_line.search([]).ids

        return {
            'type': 'ir.action.act_window',
            'res_model': 'sale.order.line',
            'view_mode': 'tree',
            'target': 'new',
            'ids': lines
        }

    def confirm_validate_delivery_order(self):
        self.state = 'sale'
        for picking in self.picking_ids:
            if picking.state == 'assigned':
                picking.button_validate()

    def _compute_if_delivery_orders_completed(self):
        for order in self:
            if order.state != 'draft':
                order.is_all_picking_completed = True if len(
                    order.picking_ids.filtered(lambda x: x.state in ['cancel', 'done'])) == len(
                    order.picking_ids.mapped('state')) else False

            else:
                order.is_all_picking_completed = False

    @api.onchange('product_tmpl_ids')
    def _onchange_product_templates(self):
        if self.product_tmpl_ids:
            for product in self.product_tmpl_ids.product_variant_ids._origin:
                if self.warehouse_id.lot_stock_id in product.stock_quant_ids.mapped(
                        'location_id') and product.stock_quant_ids.filtered(
                    lambda x: x.location_id == self.warehouse_id.lot_stock_id).available_quantity > 0:
                    self.order_line = [(0, 0, {
                        'product_id': product.id,
                        'name': product.name,
                        'price_unit': product.lst_price,
                        'product_uom': product.uom_id
                    })]
                else:
                    self.order_line = [(5, 0, 0)]
