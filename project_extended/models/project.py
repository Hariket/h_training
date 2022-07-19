from odoo import api, fields, models


class Project(models.Model):
    _inherit = "project.tags"

    tags_user_ids = fields.Many2many('res.users', compute='_compute_assigned_user',
                                     string='Tags Users Id')

    def _compute_assigned_user(self):
        for record in self:
            tasks = self.env['project.task'].search([]).filtered(lambda rec: record.id in rec.tag_ids.ids)
            task_users = tasks.mapped('user_ids')
            record.tags_user_ids = [(6, 0, task_users.ids)]
