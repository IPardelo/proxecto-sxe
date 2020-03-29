# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Cursos(models.Model):
    _name = 'cursos'
    _description = 'Cursos'

    name = fields.Char('Curso', required=True)
    description = fields.Text('Descripción')