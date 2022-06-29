# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Store(models.Model):
    _name = 'store.store'

    name = fields.Char(string='Store Name', index=True, help='any text', translate=True, size=80)
    place = fields.Char(string='Place Name')
    size = fields.Integer("Size Num")
    product_ids = fields.One2many('store.product', 'store_id')

    
