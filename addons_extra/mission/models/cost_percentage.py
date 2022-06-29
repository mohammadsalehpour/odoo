from odoo import api, fields, models, exceptions, _

class MissionCostPercentage(models.Model):
    _name = "mission.cost.percentage"

    partner_id = fields.Many2one("res.partner", required=True, domain=[('parent_id', '=', False)])
    percentage = fields.Float(required=True)

    mission_id = fields.Many2one("mission.mission", required=True)

