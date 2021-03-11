from odoo import models, fields, api


class SaleOrder_Data(models.Model):
    _inherit = 'sale.order'
    #description = fields.Char(string='Description')

    channel_order_number = fields.Char(string = 'Channel Order No.')
    payment_amount = fields.Char(string = 'Payment Amount')
    Age = fields.Float('Age', digits=(12,4))
    custom_payment_method = fields.Char(string = 'Custom Payment Method')




class Custom_Data(models.Model):
    _name = 'custom_Data'
    _description = 'new custom module'


    name = fields.Char(string = 'Name')
    age = fields.Char(string = 'Name') 