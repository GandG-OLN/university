# -*- coding: utf-8 -*-

from odoo import models, fields, api


class purchaseOrderInherit(models.Model):
    _inherit = 'purchase.order'

    word_num = fields.Char (string = "Amount In Words:", compute = '_amount_in_word')

    def _amount_in_word (self):
        for rec in self: 
            rec.word_num = str (rec.currency_id.amount_to_text (rec.amount_total))
            
            
            
class saleOrderInherit(models.Model):
    _inherit = 'sale.order'

    word_num = fields.Char (string = "Amount In Words:", compute = '_amount_in_word')

    def _amount_in_word (self):
        for rec in self: 
            rec.word_num = str (rec.currency_id.amount_to_text (rec.amount_total))
            
            

class accountMoveInherit(models.Model):
    _inherit = 'account.move'

    word_num = fields.Char (string = "Amount In Words:", compute = '_amount_in_word')
    ref_bon_client = fields.Char(string="Référence Bon Client")

    def _amount_in_word (self):
        for rec in self: 
            rec.word_num = str (rec.currency_id.amount_to_text (rec.amount_total))
