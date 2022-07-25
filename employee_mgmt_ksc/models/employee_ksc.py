# -*- coding: utf-8 -*-

from odoo import api, fields, models


class EmployeeKsc(models.Model):
    _name = 'employee.ksc'
    _description = 'Employee'

    name = fields.Char(string='Name of the Employee', required=True)
    department_id = fields.Many2one('employee.department.ksc', required=True)
    shift_id = fields.Many2one('employee.department.shift.ksc')
    job_position = fields.Char(string='Job Position of the Employee')
    salary = fields.Float('Salary', digits=(6, 2))
    hire_date = fields.Date('Hire Date')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'),
                               ('transgender)', 'Transgender)')], string='Gender')
    job_type = fields.Selection([('permanent', 'Permanent'), ('ad_hoc', 'Ad Hoc')],
                                string='Job Type')
    is_manager = fields.Boolean('Is Manager')
    manager = fields.Many2one('employee.ksc', string="Manager")
    related_user = fields.Many2one('res.users')
    increment_percentage = fields.Float('Increment Percentage')
