# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Author(models.Model):
    _inherit = 'res.partner'
    
    author_book_ids = fields.One2many('library.author.book', 'author_id', string='Author Books')
    
