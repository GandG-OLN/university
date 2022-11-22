# -*- coding: utf-8 -*-

from odoo import models, fields, api


class UniversityDepartement(models.Model):
    
    _name = 'university.departement'
     
    name = fields.Char('Nom')
    code = fields.Char('Code')
    
# One2many

    professeur_ids = fields.One2many(comodel_name='university.professeur', inverse_name='departement_id')
    matiere_ids = fields.One2many(comodel_name='university.matiere', inverse_name='departement_id')
    etudiant_ids = fields.One2many(comodel_name='university.etudiant', inverse_name='departement_id')
    