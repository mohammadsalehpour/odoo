# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class AuthorBook(models.Model):
    _name = 'library.author.book'


    book_id = fields.Many2one('library.book', required=True, string="Book")
    author_id = fields.Many2one('res.partner', required=True, string="Author")
    companionship_percentage = fields.Float(required=True, string='Companionship Percentage')
    publication_date = fields.Datetime(required=True, string='Publication Datetime')
    description = fields.Text()
    

    def name_get(self):
        result = []
        for b in self:
            res = "(Book: " + b.book_id.name + ", Author: " + b.author_id.name + " )"
            result.append((b.id, res))
        return result