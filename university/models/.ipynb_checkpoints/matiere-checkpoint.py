# -*- coding: utf-8 -*-

from odoo import models, fields, api


class UniversityMatiere(models.Model):
    
    _name = 'university.matiere'
     
    name = fields.Char('Nom')
    code = fields.Char('Code')
    
    departement_id = fields.Many2one(comodel='university.departement')
    
    professeur_ids = fields.Many2many(comodel_name='university.professeur',
                                     relation='mat_prof_rel',
                                     colum1='name',
                                     colum2='f_name')