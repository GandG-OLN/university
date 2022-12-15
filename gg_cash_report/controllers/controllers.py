# -*- coding: utf-8 -*-
# from odoo import http


# class GgCashReport(http.Controller):
#     @http.route('/gg_cash_report/gg_cash_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gg_cash_report/gg_cash_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('gg_cash_report.listing', {
#             'root': '/gg_cash_report/gg_cash_report',
#             'objects': http.request.env['gg_cash_report.gg_cash_report'].search([]),
#         })

#     @http.route('/gg_cash_report/gg_cash_report/objects/<model("gg_cash_report.gg_cash_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gg_cash_report.object', {
#             'object': obj
#         })
