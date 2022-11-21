# -*- coding: utf-8 -*-

from odoo import models, fields, api

class UniversityProfesseur(models.Model):
    
    _name = 'university.professeur'
     
    f_name = fields.Char('Prenom')
    l_name = fields.Char('Nom')
    sexe = fields.Selection([('male','Male'), ('female','Female')])
    cni = fields.Char('CNI')
    address = fields.Text('Adresse')
    birthday = fields.Date('Date de naissance')
    start_date = fields.Datetime('Date de prise de fonction')
    email = fields.Char()
    phone = fields.Char()
    
# Déclaration de champs many2one

    departement_id = fields.Many2one(comodel_name='university.departement')
    matiere_id = fields.Many2one(comodel_name='university.matiere')
    
# Déclaration de champs many2many

    classroom_ids = fields.Many2many(comodel_name='university.classroom',
                                     relation='prof_class_rel',
                                     colum1='f_name',
                                     colum2='classroom_name')
    