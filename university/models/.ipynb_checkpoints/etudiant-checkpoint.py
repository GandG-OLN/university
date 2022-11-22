# -*- coding: utf-8 -*-

from odoo import models, fields, api


class UniversityEtudiant(models.Model):
    
    
# déclartion champs simple

    _name = 'university.etudiant'
    
    name = fields.Char(compute="_get_full_name", store=True)
    f_name = fields.Char('Prenom')
    l_name = fields.Char('Nom')
    sexe = fields.Selection([('male','Male'), ('female','Female')])
    cni = fields.Char('CNI')
    address = fields.Text('Adresse')
    birthday = fields.Date('Date de naissance')
    registration_date = fields.Datetime('Date d\'inscription')
    email = fields.Char()
    phone = fields.Char()
    
#    déclaration champs Many2one 

    departement_id = fields.Many2one(comodel_name='university.departement')
    #room_id = fields.Many2one('university.classroom')
    
    @api.depends('f_name', 'l_name')
    def _get_full_name(self):
        for rec in self:
            if rec.f_name and rec.l_name:
                rec.name = rec.f_name +" "+ rec.l_name
    
    



    