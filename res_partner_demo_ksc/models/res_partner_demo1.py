from odoo import api, fields, models
from datetime import date


class ResPartnerDemo1(models.Model):
    _name = 'res.partner.demo1'
    _description = 'partner'

    name = fields.Char(string='Name', help='Name of the partner', copy=False)
    email = fields.Char(string='Email', copy=False)
    street1 = fields.Char(string='Street1', copy=False)
    street2 = fields.Char(string='Street2', copy=False)
    city = fields.Char(string='City', help='Name of the city', copy=False)
    state = fields.Char(string='State', help='Name of the state')
    zip_code = fields.Integer('zip_code')
    country = fields.Char(string='Country', help='Name of the country')
    birthdate = fields.Date('Date of birth')
    age = fields.Integer('Age', compute='calculate_age', store='True')
    weight = fields.Float('Weight')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'),
                               ('transgender', 'Transgender')], string='Gendar')
    details = fields.Html('details')
    is_spectacles = fields.Boolean('is_spectacles')
    photo = fields.Image('Profile Image')

    @api.depends('birthdate')
    def calculate_age(self):
        print("\n\n >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>. ")
        for rec in self:
            if rec.birthdate:
                rec.age = date.today().year - rec.birthdate.year - (
                        (date.today().month, date.today().day) < (rec.birthdate.month, rec.birthdate.day))
            else:
                rec.age = 0
