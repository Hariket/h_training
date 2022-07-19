from odoo import api, fields, models

class ResStateKsc1(models.Model):
    _name = 'res.state.ksc1'

    name = fields.Char(string='Name of state')
    short_code = fields.Char(string='short code of the state')
    cname = fields.Char(string='Name of the country', copy=False)
    active = fields.Boolean('Active')
