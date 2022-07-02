# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class BorrowerBook(models.Model):
    _name = 'library.borrower.book'


    book_id = fields.Many2one('library.book', required=True, string="Book")
    borrower_id = fields.Many2one('res.partner', required=True, string="Borrower")
    start_date = fields.Date(required=True)
    end_date = fields.Date(required=True)
    delivery_time = fields.Date()
    note = fields.Text()

    
    def name_get(self):
        result = []
        for b in self:
            res = "(Book: " + b.book_id.name + ", Borrower: " + b.borrower_id.name + " )"
            result.append((b.id, res))
        return result