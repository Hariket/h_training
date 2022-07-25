# -*- coding: utf-8 -*-
from odoo import api, fields, models


class EmployeeLeaveKsc(models.Model):
    _name = 'employee.leave.ksc'
    _description = 'Employee Leave Application'

    employee = fields.Many2one('employee.ksc', string='Employee')
    department = fields.Many2one('employee.department.ksc', string='Department')
    start_date = fields.Date('Start Date')
    end_date = fields.Date('End Date')
    status = fields.Selection([('draft', 'Draft'), ('approved', 'Approved'), ('refused', 'Refused'),
                               ('cancelled', 'Cancelled')], string='Status', default='draft')
    leave_description = fields.Char(string='Leave Description', required=True)
