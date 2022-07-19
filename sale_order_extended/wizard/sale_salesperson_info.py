from odoo import api, fields, models


class SaleSalespersonInfo(models.TransientModel):
    _name = 'sale.salesperson.info'

    salesperson_ids = fields.Many2many('res.users', string='Salesperson')
    from_date = fields.Date(string='From Date')
    to_date = fields.Date(string='To Date')

    def print_report(self):
        record_ids = self.env['sale.order'].search([('date_order', '>=', self.from_date),
                                                    ('date_order', '<=', self.to_date),
                                                    ('user_id', '=', self.salesperson_ids.ids),
                                                    ('state', '=', 'sale')]).ids

        data = {
            'from_date': self.from_date,
            'to_date': self.to_date,
            'salesperson_ids': self.salesperson_ids.ids,
            'sale_orders': record_ids
        }
        return self.env.ref('sale_order_extended.action_custom_report_sale_order_from_wizard').report_action(self,data=data)
