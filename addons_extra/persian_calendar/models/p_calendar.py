# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class PCalender(models.Model):
    _inherit = 'calendar.event'
    
    # author_book_ids = fields.One2many('library.author.book', 'author_id', string='Author Books')
    
    # author_book_ids = fields.One2many('library.author.book', 'author_id', string='Author Books', compute="compute_author_books")
    
    # def compute_author_books(self):
    #     for rec in self:
    #         rec.author_book_ids = len(self.env['library.book'].search([('author_ids', '=', rec.id)]).mapped("author_id"))
