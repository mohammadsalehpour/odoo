from odoo import api, fields, models, exceptions, _

class MissionMission(models.Model):
    _name = "mission.mission"
    _rec_name = "title"

    title = fields.Char(required=True)
    note = fields.Text()
    
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)

    employee_ids = fields.Many2many("hr.employee", "mission_mission_hr_employee_rel", required=True)

    cost_percentage_ids = fields.One2many("mission.cost.percentage", "mission_id")
    travel_ticket_ids = fields.One2many("mission.travel.ticket", "mission_id")
    accomodation_ids = fields.One2many("mission.accomodation", "mission_id")


    @api.constrains("employee_ids", "start_date", "end_date")
    def check_valid_mission(self):
        overlapped_mission = self.env['mission.mission'].search(['|',
                                                                 '&', ('end_date', '>=', self.start_date), ('end_date', '<=', self.end_date),
                                                                 '&', ('start_date', '>=', self.start_date), ('start_date', '<=', self.end_date)])
        overlapped_mission -= self
        overlapped_mission_employee_ids = overlapped_mission.mapped("employee_ids").ids
        for employee_id in self.employee_ids:
            if employee_id.id in overlapped_mission_employee_ids:
                raise exceptions.ValidationError("Employees have overlap!")

    @api.model
    def create(self, vals):
        rec = super(MissionMission, self).create(vals)
        if sum(rec.cost_percentage_ids.mapped("percentage")) not in [0.0, 100.0]:
            raise exceptions.ValidationError("Sum of percentages must be 100!")

        return rec

    def write(self, vals):
        res = super(MissionMission, self).write(vals)
        if sum(self.cost_percentage_ids.mapped("percentage")) not in [0.0, 100.0]:
            raise exceptions.ValidationError("Sum of percentages must be 100!")


        return res