from odoo import api, models, _


class OrderDetailsReport(models.AbstractModel):
    _name = 'report.my_sale_extended.report_sale_orders_details'

    @api.model
    def _get_report_values(self, docids, data=None):
        report = self.env['ir.actions.report']._get_report_from_name('my_sale_extended.report_sale_orders_details')
        sale_order = self.env['sale.order'].browse(data['sale_orders'])
        custom_salesperson_ids = self.env['res.users'].browse(data['custom_salesperson_ids'])

        return {
            'doc_ids': self._ids,
            'doc_model': report.model,
            'sale_order': sale_order,
            'data': data,
            'custom_salesperson_ids': custom_salesperson_ids
        }
