# -*- coding: utf-8 -*-
from odoo import api, fields, models


class EmployeePosition(models.Model):
    _name = 'employee.position'
    _description = 'employee position'

    name = fields.Char('Name')
