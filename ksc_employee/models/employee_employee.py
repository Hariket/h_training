# -*- coding: utf-8 -*-
from odoo import api, fields, models
from datetime import date
from odoo.exceptions import ValidationError


class EmployeeEmployee(models.Model):
    _name = 'employee.employee'
    _description = 'Employee'

    name = fields.Char(string='Name', help='Name of the Employee', copy=False)
    salary = fields.Float('Salary', readonly=True, default=5000)
    age = fields.Integer('Age', compute='calculate_age', store=True)
    dob = fields.Date('Date of Birth')
    education = fields.Selection([('graduate', 'Graduate'), ('pg', 'Post Graduate')],
                                 string='Education')
    bio = fields.Html('Bio')
    emp_image = fields.Image('Profile Image')
    job_position_id = fields.Many2one('employee.position', string='Job Position')
    tech_lang_ids = fields.One2many(comodel_name='known.tech.lang',
                                    inverse_name='employee_id', string='Known Tech Lang')
    hobbies_ids = fields.Many2many('employee.hobbies', 'rel_employee_emp_hobbies', 'emp_id', 'hobbie_id',
                                   'Hobbies')

    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'The Name of the employee must be unique')
    ]

    @api.model
    def create(self, values):
        '''
        with the help of this,
        if we cannot assign the value of field-education then it set the default value graduate for field-education
        :return: id
        '''
        if not values.get('education', False):
            values.update({'education': "graduate"})
        res = super(EmployeeEmployee, self).create(values)
        return res

    @api.depends('dob')
    def calculate_age(self):
        '''
        this is readonly field which is calculate age from field birthdate
        :return: True
        '''
        for rec in self:
            if rec.dob:
                rec.age = date.today().year - rec.dob.year - (
                        (date.today().month, date.today().day) < (rec.dob.month, rec.dob.day))
            else:
                rec.age = 0

    @api.onchange('education')
    def change_education(self):
        '''
            with the help of this onchange method
        it sets the value of field-salary from field-education

        '''
        for rec in self:
            if rec.education == 'graduate':
                rec.salary = 15000
            elif rec.education == 'pg':
                rec.salary = 25000
            else:
                rec.salary = 0
