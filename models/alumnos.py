# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _

class Alumnos(models.Model):
    _name = 'alumnos'
    _description = 'Control de alumnos'


    name = fields.Char('Alumno', required=True)
    dni = fields.Char('Talla', required=True)
    cursos = fields.Many2many('cursos', string='Cursos', required=True)
    direccion = fields.Char('Dirección')
    telefono = fields.Char('Teléfono')

    @api.model
    def get_cursos(self, cursos):
        return cursos.mapped('cursos.name')