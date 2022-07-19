# -*- coding: utf-8 -*-
from odoo import api, fields, models
from datetime import date


class Studentstd(models.Model):
    _name = 'student.std'
    _description = 'student'

    name = fields.Char(string='Name', help='Name of the Student', copy=False)
    age = fields.Integer('Age')
    dob = fields.Date('Date of Birth')
    subject = fields.Char(string='Subject')
    standard = fields.Selection([('ssc', 'SSC'), ('hsc', 'HSC')],
                                string='standard')
    grno = fields.Integer('GRNo')
    address = fields.Char(string='Address', copy=False)
    # technical_language_ids = fields.One2many(comodel_name='known.technical.language',
    #                                          inverse_name='student_id', string='Known Technical Languages')
    technical_language_name = fields.One2many(comodel_name='known.technical.language',
                                              inverse_name='student_name', string='Known Technical Languages')

    @api.model
    def create(self, values):
        print("\n\n values :", values)
        if not values.get('standard', False):
            values.update({'standard': "ssc"})
        res = super(Studentstd, self).create(values)
        print("\n\n>>>>>>>>>>>>> ", res)
        return res

    @api.depends('dob')
    def calculate_age(self):
        print("\n\n >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>. ")
        for rec in self:
            if rec.dob:
                rec.age = date.today().year - rec.dob.year - (
                        (date.today().month, date.today().day) < (rec.dob.month, rec.dob.day))
            else:
                rec.age = 0
