from odoo import models, fields, api



class HospitalPatient(models.Model):
    _name = 'custom.module'
    _description = 'created for custom module'

    name = fields.Char(string='Name', required= True)
    age = fields.Integer('Age')
    payment_method = fields.Text('Payment Method')
    
