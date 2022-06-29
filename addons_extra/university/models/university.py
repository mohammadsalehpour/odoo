# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class University(models.Model):
    _name = 'university.university'

    name = fields.Char(string='University Name', index=True, help='any text', translate=True, size=80)
    build_year = fields.Char(string='Build Year')
    class_count = fields.Integer(string='Class Count')
    student_ids = fields.One2many('university.student', 'university_id')
    
