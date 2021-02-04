from odoo import models, fields
class futappGol(models.Model):
    _inherit = 'futapp.gol'                                                                                                 priority = fields.Selection([
                            ('0','Low'),
                            ('1','Normal'),
                            ('2','High')],'Priority',default='1')
    kanban_state = fields.Selection([
                            ('normal', 'In Progress'),
                            ('blocked', 'Blocked'),
                            ('done', 'Ready for nextstage')],
                            'Kanban State',default='normal')