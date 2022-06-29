# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Student(models.Model):
    _name = 'university.student'

    name = fields.Char(string='Student Name', index=True, help='any text', translate=True, size=80)
    code = fields.Char(string='Student Code')
    age = fields.Char(string='Age')
    university_id = fields.Many2one('university.university', string="University")
    
