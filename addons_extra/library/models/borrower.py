# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Borrower(models.Model):
    _inherit = 'res.partner'
    
    borrower_book_ids = fields.One2many('library.borrower.book', 'borrower_id', string='Borrower Books')
    
