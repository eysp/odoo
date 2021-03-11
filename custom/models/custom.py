from odoo import models, fields, api



class SaleOrder_Data(models.Model):
    _inherit = 'sale.order'

    channel_order_number = fields.Char(string = 'Channel Order')
    payment_type = fields.Char(string = 'Payment Type')
    description_1 = fields.Char(string = 'Description 1')
    unique_id = fields.Char(string = 'Unique Id')
    check_it = fields.Boolean(string = 'check it', help= 'this is just to test booleean field')
    result = fields.Float(string='result', digits=(12,6))
    custom_payment_method  = fields.Char(string='P M')
    

class HospitalPatient(models.Model):
    _name = 'custom.module'
    _description = 'created for custom module'

    name = fields.Char(string='Name', required= True)
    age = fields.Integer('Age')
    payment_method = fields.Text('Payment Method')
    
