# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Borrower(models.Model):
    _name = 'library.borrower'

    name = fields.Char(string='Borrower Name', index=True, help='any text', translate=True, size=80)
    age = fields.Char(string='Age')
    book_ids = fields.One2many('library.borrower.book', 'borrower_id')
    
