# -*- coding: utf-8 -*-

 from odoo import models, fields, api


 class UniversityClassroom(models.Model):
     _name = 'university.classroom'
     
     name = fields.Char('Nom')
     code = fields.Char('Code')
    