# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class EmployeeEmployee(models.Model):
    _name = 'employee.employee'
    _inherit = ['employee.employee', 'portal.mixin', 'mail.thread', 'mail.activity.mixin', 'utm.mixin']

    working_exp = fields.Float('Experience', tracking=True)
    comments = fields.Text('Comment')

    @api.constrains('dob')
    def check_dob(self):
        '''
        check constraint on dob field
        this constraint is check dob
        if dob is less then 1990 then it gives validation error
        :return: True
        '''
        for rec in self:
            if rec.dob.year < 1990:
                raise ValidationError('Date of Birth Must be greater than 1990')
