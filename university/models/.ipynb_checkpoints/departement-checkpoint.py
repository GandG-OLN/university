# -*- coding: utf-8 -*-

from odoo import models, fields, api


class UniversityDepartement(models.Model):
    
    _name = 'university.departement'
     
    name = fields.Char('Nom')
    code = fields.Char('Code')
    