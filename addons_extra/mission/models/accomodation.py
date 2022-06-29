from odoo import api, fields, models, _

class MissionAccomodation(models.Model):
    _name = "mission.accomodation"
    _order = "date_from asc"

    city = fields.Char(required=True)
    date_from = fields.Date(required=True)
    date_to = fields.Date(required=True)
    image = fields.Binary()

    mission_id = fields.Many2one("mission.mission")
