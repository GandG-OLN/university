# -*- coding: utf-8 -*-

from odoo import models, fields, api


class UniversityDepartement(models.Model):
    
    _name = 'university.departement'
     
    name = fields.Char('Nom')
    code = fields.Char('Code')
    
# One2many

    professeur_ids = fiels.One2many(comodel_name='university.professeur', inverse_name='departement_id')
    matiere_ids = fiels.One2many(comodel_name='university.matiere', inverse_name='departement_id')
    