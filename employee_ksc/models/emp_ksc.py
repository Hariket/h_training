# -*- coding: utf-8 -*-
from odoo import api, fields, models


class EmpKsc(models.Model):
    _name = 'emp.ksc'
    _description = 'Employee'

    name = fields.Char(string='Name of the Employee', copy=False)
    dname = fields.Char(string='Department Name of the Employee')
    job_position = fields.Char(string='Job Position of the Employee', copy=False)
    salary = fields.Float('Salary', digits=(6, 2))
    hire_date = fields.Date('Hire Date')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'),
                               ('transgender', 'Transgender')], string='Gender')
    job_type = fields.Selection([('permanent', 'Permanent'), ('ad hoc', 'Ad Hoc')],
                                string='Job Type')
