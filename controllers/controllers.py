# -*- coding: utf-8 -*-
# from odoo import http


# class /opt/odoo/custom-addons/convalidaciones(http.Controller):
#     @http.route('//opt/odoo/custom-addons/convalidaciones//opt/odoo/custom-addons/convalidaciones/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//opt/odoo/custom-addons/convalidaciones//opt/odoo/custom-addons/convalidaciones/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/opt/odoo/custom-addons/convalidaciones.listing', {
#             'root': '//opt/odoo/custom-addons/convalidaciones//opt/odoo/custom-addons/convalidaciones',
#             'objects': http.request.env['/opt/odoo/custom-addons/convalidaciones./opt/odoo/custom-addons/convalidaciones'].search([]),
#         })

#     @http.route('//opt/odoo/custom-addons/convalidaciones//opt/odoo/custom-addons/convalidaciones/objects/<model("/opt/odoo/custom-addons/convalidaciones./opt/odoo/custom-addons/convalidaciones"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/opt/odoo/custom-addons/convalidaciones.object', {
#             'object': obj
#         })
