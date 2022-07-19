# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class StudentStd(models.Model):
    _name='student.std'
    _inherit = ['student.std', 'portal.mixin', 'mail.thread', 'mail.activity.mixin', 'utm.mixin']

    roll_no = fields.Integer('Roll No', tracking=True)
    comments = fields.Text('Comment')
    stream = fields.Char(string='Stream')

    @api.constrains('dob')
    def check_dob(self):
        for rec in self:
            if rec.dob.year < 1997:
                raise ValidationError('Date of Birth Must be greater than 1997')
