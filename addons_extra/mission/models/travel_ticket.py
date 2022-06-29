from odoo import api, fields, models, _

class MissionTravelTicket(models.Model):
    _name = "mission.travel.ticket"
    _order = "date asc"

    employee_id = fields.Many2one("hr.employee", required=True)
    date = fields.Date(required=True)
    city_from = fields.Char(required=True)
    city_to = fields.Char(required=True)
    vehicle_type = fields.Selection([('bus', 'Bus'), ('train', 'Train'), ('ride', 'Ride'), ('airplane', 'Airplaine')], required=True)
    image = fields.Binary()

    mission_id = fields.Many2one("mission.mission")
