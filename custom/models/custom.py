from odoo import models, fields, api



class SaleOrder_Data(models.Model):
    _inherit = 'sale.order'
    custom_payment_method  = fields.Char(string='P M')
    # custom_payment_method = fields.Many2one(
    #     'res.partner', string='P M', readonly=True,
    #     states={'draft': [('readonly', False)], 'sent': [('readonly', False)]},
    #     required=True, change_default=True, index=True, tracking=1,
    #     domain="['|', ('company_id', '=', False), ('company_id', '=', company_id)]",)

# class SaleReport_Data(models.Model):
#     _inherit = 'sale.report'
#     custom_payment_method  = fields.Char(string='P M')
    
    
#self.env.cr.execute("SELECT custom_payment_method FROM sale.order LEFT JOIN sale.order ON sale.order.Id = sale.report.Id")
#self.env.cr.commit()  

class HospitalPatient(models.Model):
    _name = 'custom.module'
    _description = 'created for custom module1'

    name = fields.Char(string='Name', required= True)
    age = fields.Integer('Age')
    payment_method = fields.Text('Payment Method')
    
