# -*- coding: utf-8 -*-

 from odoo import models, fields, api


 class UniversityEtudiant(models.Model):
     _name = 'university.etudiant'
     
     f_name = fields.Char('Prenom')
     l_name = fields.Char('Nom')
     sexe = fields.Selection([('male','Male'), ('female','Female')])
     cni = fields.Char('CNI')
     address = fields.Text('Adresse')
     birthday = fields.Date('Date de naissance')
     registration_date = fields.DateTime('Date d\'inscription')
     email = fields.Char()
     phone = fields.Char()
    