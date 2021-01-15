# -*- coding: utf-8 -*-

from odoo import models, fields, api


class convalidaciones_model(models.Model):
    _name = 'convalidaciones.convalidaciones_model'
    _description = 'Modulo de convalidaciones'

    fecha = fields.Date(string="Fecha",required=True,index=True,)
    modulo_id = fields.Many2one(string="Id del modulo",required=True,index=True,)
    alumno_id = fields.Many2one(string="Id del alumno",required=True,index=True,)
    
    
    
    


#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
