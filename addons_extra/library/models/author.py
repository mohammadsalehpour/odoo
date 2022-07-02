# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Author(models.Model):
    _name = 'library.author'

    name = fields.Char(string='Author Name', index=True, help='any text', translate=True, size=80)
    age = fields.Char(string='Age')
    book_ids = fields.One2many('library.book', 'author_id')
    
