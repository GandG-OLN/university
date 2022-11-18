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
     start_date = fields.DateTime('Date de prise de fonction')
     email = fields.Char()
     phone = fields.Char()
    