from odoo import _, api, fields, models

class Guia(models.Model):
    _name = 'asset.guia.turistico'
    _description = 'Modelo Guia Turistico'
    
    name = fields.Char(string='Nombre del guia')
    telefono = fields.Char(string='telefono')
    disponible = fields.Boolean(string='disponible', default=True)

    @api.onchange('telefono')
    def _onchange_telefono(self):
        if self.telefono and len(self.telefono) != 9:
            return{
                'warning':{
                    'title': "Longitud incorrecta",
                    'message': "El telefono tiene 9 caracteres"
                }
            }