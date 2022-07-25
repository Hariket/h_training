from odoo import api, fields, models


class CrmLeadLineKsc(models.Model):
    _name = 'crm.lead.line.ksc'
    _description = 'Lead'

    product_id = fields.Many2one('product.ksc')
    name = fields.Text(string='Description')
    expected_sell_qty = fields.Float('expected_sell_qty')
    uom_id = fields.Many2one('product.uom.ksc')
    lead_id = fields.Many2one('lead.ksc')

    @api.onchange('product_id')
    def _onchange_product_id(self):
        '''
        when product id is changed then the name of the product is also changed
        :return: True
        '''
        self.name = self.product_id.name
