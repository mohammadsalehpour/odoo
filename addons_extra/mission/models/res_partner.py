from odoo import api, fields, models, _

class ResPartner(models.Model):
    _inherit = "res.partner"

    missions_count = fields.Integer(compute="compute_missions_count")

    def compute_missions_count(self):
        for rec in self:
            rec.missions_count = len(self.env['mission.cost.percentage'].search([('partner_id', '=', rec.id)]).mapped("mission_id"))
