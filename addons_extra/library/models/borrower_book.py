# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class BorrowerBook(models.Model):
    _name = 'library.borrower.book'

    note = fields.Text()
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    delivery_time = fields.Date(required=True)

    book_id = fields.Many2one('library.book', string="Book")
    borrower_id = fields.Many2one('library.borrower', string="Borrower")
    
