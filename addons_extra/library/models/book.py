# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Book(models.Model):
    _name = 'library.book'

    name = fields.Char(string='Student Name', index=True, help='any text', translate=True, size=80)
    pages_count = fields.Char(string='Age')
    author_id = fields.Many2one('library.author', string="Author")
    borrower_ids = fields.One2many('library.borrower.book', 'book_id')
    
