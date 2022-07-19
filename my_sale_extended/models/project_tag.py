from odoo import fields, models, api


class ProjectTags(models.Model):
    _inherit = "project.tags"

    users_toTags_ids = fields.Many2many('res.users', compute='_compute_users_assigned_toTag')

    def _compute_users_assigned_toTag(self):
        for tag in self:
            tag.users_toTags_ids = self.env["project.task"].search([('tag_ids', '=', tag.id)]).user_id
