# -*- coding: utf-8 -*-

from odoo import models, fields, api
import random, string

class alumno_model(models.Model):
    _name = 'convalidaciones.alumno_model'
    _description = 'Modulo de alumno'

    name = fields.Char(string="Nombre",required=True,index=True,)
    password = fields.Char(string="Contraseña",required=False,index=True,)
    foto = fields.Binary()
    edad = fields.Integer(string="Edad",required=True,index=True,)
    localidad = fields.Char(string="Localidad",required=True,index=True,)
    provincia = fields.Char(string="Provincia",required=True,index=True,)
    email = fields.Char(string="Correo electronico",required=True,index=True,)


    #generar una contraseña aleatoria que se guarda en una string auxiliar y luego se le asign al password
    def generatePassword(self):
        self.ensure_one()
        aux = ''.join(random.choice( string.ascii_letters  ) for x in range(5))+''.join(random.choice( string.digits  ) for x in range(5))
        aux = ''.join(random.sample(aux,len(aux)))
        self.password = aux
        return True
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
