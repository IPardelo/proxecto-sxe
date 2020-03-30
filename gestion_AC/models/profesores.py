# -*- coding: utf-8 -*-
import logging

from odoo import models, fields, api

class Profesores(models.Model):
    _name = 'profesores'
    _description = 'Control de profesores'


    name = fields.Char('Profesor', required=True)
    dni = fields.Char('DNI', required=True)
    direccion = fields.Char('Dirección')
    telefono = fields.Char('Teléfono')
    cursos = fields.One2many('cursos', 'profesores_id', string='Cursos')

    @api.model
    def get_cursos(self, cursos):
        return cursos.mapped('cursos.name')