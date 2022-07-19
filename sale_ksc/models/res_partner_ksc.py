from odoo import api, fields, models


class ResPartnerKsc(models.Model):
    _name = 'res.partner.ksc'

    name = fields.Char(string='Name Of The Partner', required=True)
    street1 = fields.Char(string='Street 1')
    street2 = fields.Char(string='Street 2')
    country = fields.Many2one('res.country.ksc')
    state = fields.Many2one('res.state.ksc')
    city = fields.Many2one('res.city.ksc')
    zip_code = fields.Char(string='Zip Code')
    email = fields.Char(string='Email')
    mobile = fields.Char(string='Mobile')
    phone = fields.Char(string='Phone')
    photo = fields.Image('Photo')
    website = fields.Char(string='Website')
    active = fields.Boolean('Active', default=True)
    parent_id = fields.Many2one('res.partner.ksc')
    child_ids = fields.One2many('res.partner.ksc', 'parent_id')
    address_type = fields.Selection([('invoice', 'Invoice'), ('shipping', 'Shipping'),
                                     ('contact', 'Contact')], string='Address Type')
