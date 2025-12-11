# from odoo import http


# class Repaso6modulos(http.Controller):
#     @http.route('/repaso6modulos/repaso6modulos', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/repaso6modulos/repaso6modulos/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('repaso6modulos.listing', {
#             'root': '/repaso6modulos/repaso6modulos',
#             'objects': http.request.env['repaso6modulos.repaso6modulos'].search([]),
#         })

#     @http.route('/repaso6modulos/repaso6modulos/objects/<model("repaso6modulos.repaso6modulos"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('repaso6modulos.object', {
#             'object': obj
#         })

