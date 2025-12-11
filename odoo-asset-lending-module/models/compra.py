from odoo import _, api, fields, models
import random
import string
from datetime import date

class Compra(models.Model):
    _name = 'asset.compra'
    _description = 'Modelo Compra'

    def _get_random(self):
        caracteres = string.ascii_uppercase + string.digits
        codigo = ""
        for i in range(8):
            codigo += random.choice(caracteres)
        return codigo
    
    codigo_reserva = fields.Char(string='codigo_reserva', default=_get_random, readonly=True)
    fecha_inscripcion = fields.Date(string='Fecha_inscripcion', default=fields.Date.today)

    alumno_id = fields.Many2one('asset.alumno', string='Alumno')
    viaje_id = fields.Many2one('asset.viaje', string='Viaje')

    precio_final = fields.Float(compute='_compute_precio_final', string='precio_final')
    
    @api.depends('viaje_id', 'fecha_inscripcion')
    def _compute_precio_final(self):
        for c in self:
            if c.viaje_id and c.fecha_inscripcion:
                precio = c.viaje_id.precio_base

                antelacion = c.fecha_inscripcion - c.viaje_id.fecha_salida

                if antelacion.days > 30:
                    c.precio_final = precio * 0.90
                else:
                    c.precio_final = precio
            else:
                c.precio_final = 0.0

    @api.onchange('alumno_id')
    def _onchange_alumno_id(self):
        if self.alumno_id:
            fecha_p = self.alumno_id.fecha_caducidad_pasaporte

            if fecha_p and fecha_p < date.today():
                return{
                    'warning':{
                        'title': "Pasaporte caducado",
                        'message': "Cuidado el alumno tiene el pasaporte caducado"
                    }
                }