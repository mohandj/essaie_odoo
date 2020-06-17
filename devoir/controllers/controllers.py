# -*- coding: utf-8 -*-
# from odoo import http


# class Devoir(http.Controller):
#     @http.route('/devoir/devoir/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/devoir/devoir/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('devoir.listing', {
#             'root': '/devoir/devoir',
#             'objects': http.request.env['devoir.devoir'].search([]),
#         })

#     @http.route('/devoir/devoir/objects/<model("devoir.devoir"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('devoir.object', {
#             'object': obj
#         })
