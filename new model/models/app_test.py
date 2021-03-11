from odoo import models, fields, api



class TestModel_Data(models.Model):
      _name = 'Test.data'
      _description = 'Test records'

       test_name = fields.Char(string = 'Name')
       Age = fields.Float('Age', digits=(12,4))