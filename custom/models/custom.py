from odoo import models, fields, api



class SaleOrder_Data(models.Model):
    _inherit = 'sale.order'
    custom_payment_method  = fields.Char(string='P M')

# class SaleReport_Data(models.Model):
#     _inherit = 'sale.report'
#     custom_payment_method  = fields.Char(string='P M')
    
    
#self.env.cr.execute("SELECT custom_payment_method FROM sale.order LEFT JOIN sale.order ON sale.order.Id = sale.report.Id")
#self.env.cr.commit()  

class HospitalPatient(models.Model):
    _name = 'custom.module'
    _description = 'created for custom module'

    name = fields.Char(string='Name', required= True)
    age = fields.Integer('Age')
    payment_method = fields.Text('Payment Method')
    
