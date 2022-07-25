# -*- coding: utf-8 -*-
from odoo import api, fields, models


class EmployeeDepartmentShiftKsc(models.Model):
    _name = 'employee.department.shift.ksc'
    _description = 'Employee Department Shift'

    shift = fields.Selection([('morning', 'Morning'), ('afternoon', 'Afternoon'),
                              ('evening', 'Evening'), ('night', 'Night')], string='Shift')
    employee_ids = fields.One2many(comodel_name='employee.ksc',
                                    inverse_name='shift_id', string='Employee')
