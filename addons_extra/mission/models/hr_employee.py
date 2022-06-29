from odoo import api, fields, models, _

class HREmployee(models.Model):
    _inherit = "hr.employee"

    mission_ids = fields.Many2many("mission.mission", "mission_mission_hr_employee_rel", readonly=True)

