

from odoo import models, fields

class HelpdeskTicket(models.Model):
	_name = 'helpdesk.ticket'
	_description = "Helpdesk Ticket"
	
	name = fields.Char(
		string='Name',
		required=True)	
		
	description = fields.Text(
		string='Description')
	date = fields.Date(
		string='Date')
	#Estado [Nuevo, Asignado, En proceso, Pendiente, Resuelto, Cancelado], que por defecto sea Nuevo
	state = fields.Selection(
		[('new', 'New'),
		('assigned', 'Assigned'),
		('progress', 'Progress'),
		('waiting', 'Waiting'),
		('done', 'Done'),
		('cancel', 'Cancel')],
		string='State',
		default='new')
		
	#Tiempo dedicado (en horas)
	dedicated_time = fields.Float(
	string='Time')
	
	#Asignado (tipo check)
	assigned = fields.Boolean(
	string='Assigned',
	readonly=True)
	
	#Fecha límite
	date_due = fields.Date(
	string='Date Due')
	
	#Acción correctiva (html)
	corrective_action = fields.Html(
	help='Detail of corrective action after this issue')
	#Acción preventiva (html)
	preventive_action = fields.Html(
	help='Detail of preventive action after this issue')
