# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ResCityKsc(models.Model):
    _name = 'res.city.ksc'
    _description = 'res.city.ksc'

    name = fields.Char(string='Name of City')
    country_id = fields.Many2one('res.country.ksc')