from odoo import api, models, _


class SaleorderWizard(models.AbstractModel):
    _name = 'report.sale_order_extended.report_saleorder_wizard'

    @api.model
    def _get_report_values(self, docids, data=None):
        report = self.env['ir.actions.report']._get_report_from_name('sale_order_extended.report_saleorder_wizard')
        sale_order = self.env['sale.order'].browse(data['sale_orders'])
        salesperson_ids = self.env['res.users'].browse(data['salesperson_ids'])

        return {
            'doc_ids': self._ids,
            'doc_model': report.model,
            'sale_order': sale_order,
            'data': data,
            'salesperson_ids': salesperson_ids
        }
