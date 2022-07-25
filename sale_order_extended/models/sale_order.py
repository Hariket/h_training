from odoo import api, fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    custom_crm_lead_id = fields.Many2one('crm.lead')
    is_all_picking_completed = fields.Boolean('is_all_picking_completed', store=False)
    product_tmpl_ids = fields.Many2many('product.template')

    def scan_all_sale_order_line(self):
        '''
        Button: Scan
        when the button is clicked then it shows other orderes which is in sale state
        '''
        orders = self.search(
            ['&', ('state', '=', 'sale'),
             ('order_line.product_id', 'in', self.mapped('order_line.product_id.id'))
             ])
        if orders:
            action = self.env["ir.actions.actions"]._for_xml_id("sale.action_orders")
            action['domain'] = [('id', 'in', orders.ids)]
        return action
