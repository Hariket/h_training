# -*- coding: utf-8 -*-
from odoo import api, fields, models


class EmployeeEmployee(models.Model):
    _name = 'employee.hobbies'

    name = fields.Char('Name')