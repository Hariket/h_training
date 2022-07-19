from odoo import api, fields, models

class ResCountryKsc1(models.Model):
    _name = 'res.country.ksc1'

    name = fields.Char(string='Name of country')
    short_code = fields.Char(string='short code of the country')
    active = fields.Boolean('Active')
