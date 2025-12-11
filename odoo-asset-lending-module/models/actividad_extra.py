from odoo import _, api, fields, models
from datetime import date
from odoo.exceptions import ValidationError

class ActividadExtra(models.Model):
    _name = 'asset.actividad.extra'
    _description = 'Modelo Actividad Extra'

    name = fields.Char(string='name')
    fecha_realizacion = fields.Date(string='fecha_realizacion')
    
    viaje_ids = fields.Many2many('asset.viaje', string='viaje')

    @api.constrains('fecha_realizacion', 'viaje_ids')
    def _constrains_fecha_realizacion(self):
        for ae in self:
            if ae.fecha_realizacion:
                if ae.fecha_realizacion < date.today():
                    raise ValidationError("La actividad no puede ser anterior a hoy")
                
                f_inicio_viaje = ae.viaje_ids.fecha_salida
                f_fin_viaje = ae.viaje_ids.fecha_regreso

                if f_inicio_viaje and f_fin_viaje:
                    if ae.fecha_realizacion < f_inicio_viaje:
                        raise ValidationError("La actividad no puede ser antes que el viaje")
                    
                    if ae.fecha_realizacion > f_fin_viaje:
                        raise ValidationError("La actividad no puede ser despues que el viaje")