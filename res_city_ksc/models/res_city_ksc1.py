from odoo import api, fields, models


class ResCityKsc1(models.Model):
    _name = 'res.city.ksc1'
    _description = 'City'

    name = fields.Char(string='Name of the city')
    short_code = fields.Char(string='short code of the city')
    sname = fields.Char(string='Name of the state')
    cname = fields.Char(string='Name of the country')
    active = fields.Boolean('Active')
