from odoo import models,fields
class TodoTask(models.Model):
    __name = 'todo.task'
    __description = 'to task description'

    name= fields.Char('Task Name',required=True)
    description = fields.Char('Task Description',required=True)
    due_date= fields.Date(string='')
    done= fields.Boolean( 'Completed',default=False)
