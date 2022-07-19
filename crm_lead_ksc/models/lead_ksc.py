# -*- coding: utf-8 -*-
from odoo import api, fields, models


class LeadKsc(models.Model):
    _name = 'lead.ksc'

    name = fields.Char(string='Name of the Customer', copy=False, required=True)
    email = fields.Char(string='Email of the Customer', copy=False, required=True)
    phone = fields.Char(string='phone of the Customer', copy=False, required=True)
    expected_revenue = fields.Float('Expected revenue', digits=(14, 3))
    salesperson = fields.Char(string='Name of the Salesperson', copy=False, required=True)
    sales_team = fields.Char(string='Sales Team')
    tag_ids = fields.Float('tag_ids')
    color = fields.Integer("Color Index", default=0)
    priority = fields.Selection([('0', 'very low'), ('1', 'low'), ('2', 'medium'),
                                 ('3', 'high'), ('4', 'very high')], string='priority')
    activity_state = fields.Selection([('active', 'Active'), ('deactivate', 'Deactivate')],
                                      string='activity_state')
    campaign = fields.Char(string='Campaign')
    channel = fields.Selection([('facebook', 'Facebook'), ('whatsApp', 'WhatsApp'),
                                ('email', 'Email'), ('newspaper', 'Newspaper'),
                                ('television', 'Television'), ('phone call', 'Phone Call'),
                                ('sms', 'SMS'), ('google ads', 'Google Ads')],
                               string='channel', required=True)
    state = fields.Selection([('new', 'New'), ('qualified', 'Qualified'),
                              ('proposition', 'Proposition'), ('won', 'Won'),
                              ('lost', 'Lost')], string='state')
    won_date = fields.Date("Won Date")
    lost_reason = fields.Char('Lost Reason')
