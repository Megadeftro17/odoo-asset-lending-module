from odoo import _, api, fields, models
from odoo.exceptions import ValidationError

class SeguroViaje(models.Model):
    _name = 'asset.seguro.viaje'
    _description = 'Modelo seguro de viaje'

    name = fields.Char(string='Nombre compañia')
    precio = fields.Float(string='Precio')

    tipo_cobertura = fields.Selection([
        ('basico', 'Basico'),
        ('completo','Completo'),
        ('premium','Premium')
    ], string='tipo_cobertura')
    
    compra_id = fields.Many2one('asset.compra', string='Inscripcion')

    @api.constrains('precio','tipo_cobertura')
    def _constrains_precio_premium(self):
        for sv in self:
            if sv.precio and sv.tipo_cobertura:
                if sv.tipo_cobertura == 'premium':
                    if sv.precio <= 50:
                        raise ValidationError("El seguro premium minimo cuesta 50")