# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Book(models.Model):
    _name = 'library.book'

    name = fields.Char(string='Book Name', index=True, help='any text', translate=True, size=80)
    serial = fields.Integer(string='Serial Num')
    isbn = fields.Float(string='ISBN Code')
    pages_count = fields.Char(string='Number Of Pages')
    author_ids = fields.One2many('library.author.book', 'book_id', string="Author")
    borrower_ids = fields.One2many('library.borrower.book', 'book_id', string="Borrowers")
    
