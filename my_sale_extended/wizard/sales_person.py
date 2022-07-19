from odoo import fields, models, api, _


class SalesPerson(models.TransientModel):
    _name = 'salesperson.wizard'

    current_user = fields.Many2one('res.users', 'Current User', default=lambda self: self.env.user)
    from_date = fields.Date()
    to_date = fields.Date()
    custom_salesperson_ids = fields.Many2many('res.users', relation='salesperson_wizard_res_users_rel')

    def print_report(self):
        record_ids = self.env['sale.order'].search([('date_order', '>=', self.from_date),
                                                         ('date_order', '<=', self.to_date),
                                                         ('user_id', '=', self.custom_salesperson_ids.ids),
                                                         ('state', '=', 'sale')]).ids
        data = {
            'current_user': self.current_user.name,
            'from_date': self.from_date,
            'to_date': self.to_date,
            'custom_salesperson_ids': self.custom_salesperson_ids.ids,
            'sale_orders': record_ids
        }
        return self.env.ref('my_sale_extended.action_custom_report_sale_order_from_wizard').report_action(self,
                                                                                                          data=data)
