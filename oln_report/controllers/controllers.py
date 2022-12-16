# -*- coding: utf-8 -*-
# from odoo import http


# class OlnReport(http.Controller):
#     @http.route('/oln_report/oln_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/oln_report/oln_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('oln_report.listing', {
#             'root': '/oln_report/oln_report',
#             'objects': http.request.env['oln_report.oln_report'].search([]),
#         })

#     @http.route('/oln_report/oln_report/objects/<model("oln_report.oln_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('oln_report.object', {
#             'object': obj
#         })
