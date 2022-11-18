# -*- coding: utf-8 -*-

 from odoo import models, fields, api


 class UniversityMatiere(models.Model):
     _name = 'university.matiere'
     
     name = fields.Char('Nom')
     code = fields.Char('Code')
    