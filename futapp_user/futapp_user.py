#-*- coding: utf-8 -*-
from odoo import models, fields, api
class futappGol(models.Model):
    _name = 'futapp.gol'
    _inherit = ['futapp.gol','mail.thread']
    user_id = fields.Many2one('res.users', 'Responsible')
    date_deadline = fields.Date('Deadline')
    name = fields.Char(help="Breve descripcion de la tarea.")

    def do_marcar(self):
       if self.user_id != self.env.user:
          raise Exception('Solo el responsable ha de marcarla como hecha!')
       else:
          return super(futappGol, self).do_marcar()

    def do_limpiar(self):
       domain = [('is_done', '=', True), '|', ('user_id','=', self.env.uid), ('user_id', '=', False)]
       done_recs = self.search(domain)
       done_recs.write({'active': False})
       return True