from odoo import models, fields, api


class App_abc_data(models.Model):
	_name = 'abc.test'
	_description = 'abc records'


	abc_name = fields.Char(string = 'Name')
	abc_age = fields.Char(string = 'Age')