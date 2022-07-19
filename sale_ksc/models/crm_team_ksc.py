from odoo import api, fields, models


class CrmTeamKsc(models.Model):
    _name = 'crm.team.ksc'

    name = fields.Char(string='Name')
    team_leader = fields.Many2one('res.users', string='Team Leader')
