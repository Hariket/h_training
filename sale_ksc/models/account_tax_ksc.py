from odoo import api, fields, models


class AccountTaxKsc(models.Model):
    _name = 'account.tax.ksc'
    _description = 'Tax'

    name = fields.Char(string='Name')
    tax_use = fields.Selection([('none', 'None'), ('Sales', 'Sales'), ('purchase', 'Purchase')],
                               string='Tax Use')
    tax_value = fields.Float('Tax Value')
    tax_amount_type = fields.Selection([('percentage', 'Percentage'), ('fixed', 'Fixed')],
                                       string='Tax Amount Type', default='fixed')


