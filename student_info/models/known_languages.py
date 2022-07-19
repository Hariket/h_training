# -*- coding: utf-8 -*-

from odoo import api, fields, models


class KnownTechnicalLanguage(models.Model):
    _name = 'known.technical.language'
    _description = 'known.technical.language'

    name = fields.Char('Name')
    # student_id = fields.Many2one('student.std')
    student_name = fields.Many2one('student.std')