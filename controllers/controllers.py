# -*- coding: utf-8 -*-
# from odoo import http


# class DelPortalModify(http.Controller):
#     @http.route('/del_portal_modify/del_portal_modify', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/del_portal_modify/del_portal_modify/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('del_portal_modify.listing', {
#             'root': '/del_portal_modify/del_portal_modify',
#             'objects': http.request.env['del_portal_modify.del_portal_modify'].search([]),
#         })

#     @http.route('/del_portal_modify/del_portal_modify/objects/<model("del_portal_modify.del_portal_modify"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('del_portal_modify.object', {
#             'object': obj
#         })
