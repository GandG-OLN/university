# -*- coding: utf-8 -*-
{
    'name': "oln_report",

    'summary': """
        oln_report module for custom report""",

    'description': """
        oln_report module for custom report
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase', 'sale_management', 'sale_project'],

    # always loaded
    'data': [
        #'security/ir.model.access.csv',
        #'views/views.xml',
        'views/external_layout.xml',
        #'views/templates.xml',
        #'views/custom.xml',
        #'views/custom_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
