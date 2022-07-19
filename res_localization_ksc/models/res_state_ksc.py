# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.exceptions import ValidationError


class ResStateKsc(models.Model):
    _name = 'res.state.ksc'
    _description = 'res.state.ksc'

    name = fields.Char(string='Name of State')
    country_id = fields.Many2one('res.country.ksc')
    state_code = fields.Char(string='State Code for The State')

    @api.constrains('state_code')
    def _check_state_code(self):
        available_code = self.search([('id', '!=', self.id)]).mapped('state_code')
        print("\n\nAvailable Code>>>>>>>>>>", available_code)
        if self.state_code in available_code:
            raise ValidationError("State code must be unique.")


