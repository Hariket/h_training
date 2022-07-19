from odoo import fields, models, api


class CrmLead(models.Model):
    _inherit = "crm.lead"

    def action_sale_quotations_new(self):
        action = super(CrmLead, self).action_sale_quotations_new()
        action['context'].update({'default_custom_opportunity_crm_lead_id': self.id,
                                  'default_custom_opportunity_tag_ids': [
                                      (6, 0,
                                       [self.env.ref('my_sale_extended.data_crm_tag_ids_id').id]
                                       )]
                                  })
        return action
