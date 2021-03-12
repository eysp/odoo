from odoo import models, fields, api


class SaleOrder_Data(models.Model):
    _inherit = 'sale.order'
    #description = fields.Char(string='Description')

    custom_payment_method = fields.Many2one('custom.module',string = 'Custom Payment Method')




class Custom_Data(models.Model):
    _name = 'custom.module'
    _description = 'new custom module'


    name = fields.Char(string = 'Name')
    age = fields.Many2one('sale.order') 