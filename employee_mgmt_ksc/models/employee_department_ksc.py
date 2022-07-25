# -*- coding: utf-8 -*-
from odoo import api, fields, models


class EmployeeDepartmentKsc(models.Model):
    _name = 'employee.department.ksc'
    _description = 'Employee Department'

    name = fields.Char(string='Name of the Department', required=True)
    employee_ids = fields.One2many(comodel_name='employee.ksc',
                                   inverse_name='department_id', string='Employees')
    res_users_name = fields.Many2one('res.users', string='Department Manager')
