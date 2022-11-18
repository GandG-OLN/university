# -*- coding: utf-8 -*-
{
    'name': "university",

    'summary': """
        Test de creation de module""",

    'description': """
        Module pour la gestion d'une université
    """,

    'author': "OLN #NADMAN",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Project Management',
    'version': '0.2',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/etudiant_views.xml',
        'views/professeur_views.xml',
        'views/matiere_views.xml',
        'views/classroom_views.xml',
        'views/departement_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
