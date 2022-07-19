from odoo import api, fields, models


class CrmLeadKsc(models.Model):
    _inherit = 'lead.ksc'

    partner_id = fields.Many2one('res.partner.ksc')
    order_ids = fields.One2many(comodel_name='sale.order.ksc',
                                inverse_name='crm_lead_id', string='Order')
    lead_line_ids = fields.One2many(comodel_name='crm.lead.line.ksc',
                                    inverse_name='lead_id', string='Lead')

    def write(self, vals):
        res = super(CrmLeadKsc, self).write(vals)
        print("test", self.channel)
        print("/n>>>>>>>>>>>>>>>>>>.hhhhhhhhh",
              dict(self._fields['channel'].selection).get(self.channel))
        return res

    def button_in_won(self):
        self.update({
            'state': 'won'
        })

    def button_in_lost(self):
        self.update({
            'state': 'lost'
        })

    # def action_sale_quotations_new(self):
    #     if not self.partner_id:
    #         return self.env["ir.actions.actions"]._for_xml_id("sale_crm.crm_quotation_partner_action")
    #     else:
    #         return self.action_new_quotation()
