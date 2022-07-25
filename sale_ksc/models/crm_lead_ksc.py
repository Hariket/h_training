from odoo import api, fields, models


class CrmLeadKsc(models.Model):
    _inherit = 'lead.ksc'
    _description = 'Lead'

    partner_id = fields.Many2one('res.partner.ksc')
    order_ids = fields.One2many(comodel_name='sale.order.ksc',
                                inverse_name='crm_lead_id', string='Order')
    lead_line_ids = fields.One2many(comodel_name='crm.lead.line.ksc',
                                    inverse_name='lead_id', string='Lead')

    def button_in_won(self):
        '''
        Button: Won
        when the button is clicked then the state is goes to the won state and after that the button is disappear
        '''
        self.update({
            'state': 'won'
        })

    def button_in_lost(self):
        '''
        Button: Lost
        when the button is clicked then the state is goes to the lost state and after that the button is disappear
        '''
        self.update({
            'state': 'lost'
        })
