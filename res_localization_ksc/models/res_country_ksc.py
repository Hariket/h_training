from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ResCountryKsc(models.Model):
    _name = 'res.country.ksc'

    name = fields.Char(string='Name of country')
    short_code = fields.Char(string='short code of the country')
    states_ids = fields.One2many(comodel_name='res.state.ksc',
                                 inverse_name='country_id', string='States')
    cities_ids = fields.One2many(comodel_name='res.city.ksc',
                                 inverse_name='country_id', string='Cities')

    _sql_constraints = [
        ('short_code_uniq', 'unique (short_code)', 'The Short Code of the Country must be unique')
    ]
