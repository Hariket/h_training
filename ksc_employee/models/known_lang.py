# -*- coding: utf-8 -*-

from odoo import api, fields, models


class KnownTechLang(models.Model):
    _name = 'known.tech.lang'
    _description = 'known.tech.lang'

    name = fields.Char('Name')
    employee_id = fields.Many2one('employee.employee')