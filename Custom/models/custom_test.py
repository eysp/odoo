from odoo import models, fields, api


class SaleOrder_Data(models.Model):
    _inherit = 'sale.order'
    #description = fields.Char(string='Description')

    #custom_payment_method = fields.Many2one('custom.module',string = 'Custom Payment Method')
    custom_payment_method = fields.Char(string = 'Custom Payment Method')

    #def init(self, cr):
    #	cr.execute("SELECT custom_payment_method FROM sale.order LEFT JOIN sale.report ON sale.order.Id = sale.report.id")



class Custom_Data(models.Model):
    _name = 'custom.module'
    _description = 'new custom module'


    name = fields.Char(string = 'Name')
    age = fields.Char(string = 'Age') 
    #age = fields.Many2one('sale.order') 