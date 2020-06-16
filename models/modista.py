# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Modista(models.Model):
    _name = 'modista'
    _description = 'Modista'

    name = fields.Char('Modista', required=True)
    direccion = fields.Char('Direccion')
    telefono = fields.Char('Telefono')
    category_id = fields.Many2one('categorias', string='Especialización')
