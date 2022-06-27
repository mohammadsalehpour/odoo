# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Users(models.Model):
    _name = 'university.master'

    name = fields.Char(string="")
    age = fields.Char(string="")
    build_year = fields.Integer()
