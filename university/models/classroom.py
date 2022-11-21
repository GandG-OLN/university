# -*- coding: utf-8 -*-

from odoo import models, fields, api


class UniversityClassroom(models.Model):
    
    _name = 'university.classroom'
     
    name = fields.Char('Nom')
    code = fields.Char('Code')
    
    etudiant_ids = fields.One2many(comodel_name='university.etudiant', inverse_name='classroom_id')
    
    professeur_ids = fields.Many2many(comodel_name='university.professeur',
                                     relation='class_prof_rel',
                                     colum1='classroom_name',
                                     colum2='prof_name')
    
    matiere_ids = fields.Many2many(comodel_name='university.matiere', relation='class_mat_rel', colum1='classroom_name', colum2='matiere_name')