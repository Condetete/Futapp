# -*- coding: utf-8 -*-
from odoo import models, fields
class futappGol(models.Model):
  _name = 'futapp.gol'
  _description = 'Goleadores'
  name = fields.Char('Equipos', required=True)
  name2 = fields.Char('Goleadores', required=True)
  is_done = fields.Boolean('¿Maximo Goleador del equipo?',default=True )
  active = fields.Boolean('Jugador clave', default=True)

 def do_marcar(self):
    self.is_done = not self.is_done
    return True
 def do_limpiar(self):
    done_recs = self.search([('is_done', '=', True)])
    done_recs.write({'active': False})
    return True





