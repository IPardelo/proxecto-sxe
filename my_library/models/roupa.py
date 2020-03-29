# -*- coding: utf-8 -*-
import logging

from datetime import time, datetime
from odoo import models, fields, api
from odoo.exceptions import UserError
from odoo.tools.translate import _


logger = logging.getLogger(__name__)


class Roupa(models.Model):
    _name = 'roupa'
    _description = 'Roupa'
    _defaults = {
        'date_updated': lambda *a: time.strftime('%Y-%m-%d %H:%M:%S')
    }

    name = fields.Char('Prenda', required=True)
    talla = fields.Char('Talla', required=True)
    category_id = fields.Many2one('categorias', string='Categoria')
    alumno = fields.Many2one('res.users', 'Ultimo usuario', default=lambda self: self.env.user, readonly=True)
    date_updated = fields.Datetime('Ultimo uso', readonly=True)
    modista_id = fields.Many2one('modista', string='Modista')

    state = fields.Selection([
        ('prestada', 'Prestada'),
        ('almacen', 'En almacén'),
        ('modista', 'Na modista')],
        'State', default="almacen")

    @api.model
    def is_allowed_transition(self, old_state, new_state):
        allowed = [('modista', 'almacen'),
                   ('almacen', 'prestada'),
                   ('prestada', 'almacen'),
                   ('almacen', 'modista')]
        return (old_state, new_state) in allowed

    @api.multi
    def change_state(self, new_state):
        for prenda in self:
            if prenda.is_allowed_transition(prenda.state, new_state):
                prenda.state = new_state
                self.alumno = self.env.uid
                self.date_updated = datetime.today()
            else:
                message = _('Pasar de %s a %s non está permitido') % (prenda.state, new_state)
                raise UserError(message)

    def prestada(self):
        self.change_state('prestada')

    def almacen(self):
        self.change_state('almacen')

    def modista(self):
        self.change_state('modista')