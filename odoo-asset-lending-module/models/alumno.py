from odoo import _, api, fields, models
from datetime import date,timedelta
from odoo.exceptions import ValidationError

class Alumno(models.Model):
    _name = 'asset.alumno'
    _description = 'Modelo alumno'

    nombre = fields.Char(string='Nombre')
    fecha_nacimiento = fields.Date(string='fecha_nacimiento')
    pasaporte = fields.Char(string='pasaporte')
    fecha_caducidad_pasaporte = fields.Date(string='Fecha_caducidad_pasaporte')

    compra_ids = fields.One2many('asset.compra', 'alumno_id', string='Compras')

    edad = fields.Integer(compute='_compute_edad', string='edad')
    
    @api.depends('fecha_nacimiento')
    def _compute_edad(self):
        for a in self:
            if a.fecha_nacimiento:
                today = date.today()
                a.edad = today.year - a.fecha_nacimiento.year
            else:
                a.edad = 0
    

    @api.constrains('fecha_caducidad_pasaporte')
    def _constrains_fecha_caducidad_pasaporte(self):
        for a in self:
            if a.fecha_caducidad_pasaporte:
                fecha_limite = date.today() + timedelta(days=180)

                if a.fecha_caducidad_pasaporte < fecha_limite:
                    raise ValidationError("El pasaporte debe de tener 6 meses de vigencia")