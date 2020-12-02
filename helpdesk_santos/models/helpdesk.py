from odoo import models, fields


class HelpdeskTicket(models.Model):
    _name = 'helpdesk.ticket'
    _description = "Helpesk Ticket"

    name = fields.Char(
        string='Name',
        required=True)
    description = fields.Text(
        string='Description')
    date = fields.Date(
        string='Date')
    state = fields.Selection(
        [('new', 'New'),
         ('assigned', 'Assigned'),
         ('progress', 'Progress'),
         ('waiting', 'Waiting'),
         ('done', 'Done'),
         ('cancel', 'Cancel')],
        string='State',
        default='new')
        
    dedicated_time = fields.Float(
        string='Time')

    assigned = fields.Boolean(
        string='Assigned',
        readonly=False)

    date_due = fields.Date(
        string='Date Due')

    corrective_action = fields.Html(
        help='Detail of corrective action after this issue'
    )
    preventive_action = fields.Html(
        help='Detail of preventive action after this issue')

    def set_assigned_multi(self):
        for ticket in self:
            ticket.set_assigned()

    # Asignar, cambia estado a asignado y pone a true el campo asignado, visible sólo con estado = nuevo
    def set_assigned(self):
        self.ensure_one()
        self.write({
            'assigned': True,
            'state': 'assigned',
        })
    # En proceso, visible sólo con estado = asignado
    def set_progress(self):
        self.ensure_one()
        self.state = "progress"

    # Pendiente, visible sólo con estado = en proceso o asignado
    def set_waiting(self):
        self.ensure_one()
        self.state = "waiting"    
    # Finalizar, visible en cualquier estado, menos cancelado y finalizado
    def set_done(self):
        self.ensure_one()
        self.state = "done"    
    # Cancelar, visible si no está cancelado  
    def set_cancel(self):
        self.ensure_one()
        self.state = "cancel"    
