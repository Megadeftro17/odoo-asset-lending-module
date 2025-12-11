from odoo import _, api, fields, models
from datetime import date
from odoo.exceptions import ValidationError

class Viaje(models.Model):
    _name = 'asset.viaje'
    _description = 'Modelo viajes'

    name = fields.Char(string='Nombre')
    fecha_salida = fields.Date(string='fecha_salida')
    fecha_regreso = fields.Date(string='fecha_regreso')
    precio_base = fields.Float(string='Precio Base')

    compra_ids = fields.One2many('asset.compra', 'viaje_id', string='Compras')

    duracion_dias = fields.Integer(compute='_compute_duracion_dias', string='Duracion_dias')
    
    @api.depends('fecha_regreso','fecha_salida')
    def _compute_duracion_dias(self):
        for v in self:
            if v.fecha_regreso and v.fecha_salida:
                diferencia = v.fecha_regreso - v.fecha_salida
                v.duracion_dias = diferencia.days
            else:
                v.duracion_dias = 0
    
    @api.constrains('fecha_regreso','fecha_salida')
    def _constrains_fecha_regreso(self):
        for v in self:
            if v.fecha_salida:
                if v.fecha_salida < date.today():
                    raise ValidationError("No puedes crear un viaje en el pasado")
            
            if v.fecha_salida and v.fecha_regreso:
                if v.fecha_regreso < v.fecha_salida:
                    raise ValidationError("La fecha de regreso tiene que ser posterior")

    actividad_extra_ids = fields.Many2many('asset.actividad.extra', string='actividad_extra')