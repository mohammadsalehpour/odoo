# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Product(models.Model):
    _name = 'store.product'

    name = fields.Char(string='Product Name', index=True, help='any text', translate=True, size=80)
    price = fields.Char(string='Price')
    color = fields.Char(string='Color')
    store_id = fields.Many2one('store.store', string="Store")
    
