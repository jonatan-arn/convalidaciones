# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ciclo_model(models.Model):
    _name = 'convalidaciones.ciclo_model'
    _description = 'Modulo de ciclos'

    name = fields.Char(string="Nombre del modulo",required=True,index=True,)
    descripcion = fields.Char(string="Descripción",required=True,index=True,)


#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
