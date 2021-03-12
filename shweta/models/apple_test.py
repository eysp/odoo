from odoo import models, fields

class Task(models.Model):
   _inherit = "project.task"
   task_tag_id = fields.Many2one('project.task.tag', string='Task Tag')
class ProjectTaskTag(models.Model):
   _name = "project.task.tag"
   task_id = fields.Many2one('project.task')
   name = fields.Char(string='Name')