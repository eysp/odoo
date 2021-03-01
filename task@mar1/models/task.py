from odoo import api, fields, models

class Task_purchase(models.Model):
    _inherit = 'purchase.order'

    def create_sales_order(self):
        # order_reference = self.name

        # line_items_vals = []
        # for line in self.line_items:
        #     line_items_vals.append({
        #         'product_id': line.product_id.id,
        #         'name': line.name,
        #         'product_uom_qty': line.product_qty,
        #         'price_unit': line.price_unit,
        #         'line_project_focus' : line.line_project_focus.id
        #     })

        vals = {
            'partner_id' : self.partner_id.id,  
            # 'freight_supplier_currency' : self.freight_supplier_currency,
            # 'exchange_rate' : self.supplier_client_exchange_rate,
            # 'design_engineering' : self.design_engineering, 
            # 'commissioning' : self.commissioning,
            # 'handlings' : self.handlings,
            # 'custom_value' : self.custom_value,
            # 'project_focus' : self.project_focus.id,
            # 'standard_sale_order' : False,
            # 'order_line' : [(0, 0, invoice_line_id) for invoice_line_id in line_items_vals]
        }

        # print("**************************************** *************************************
        # print(self.partner_id.id)

        view_ref = self.env['ir.model.data'].get_object_reference('sale', 'view_order_form')
        view_id = view_ref[1] if view_ref else False

        new_salesorder = self.env['sale.order'].create(vals)
    
        view_data = {
        'type': 'ir.actions.act_window',
        'name': ('Sales Order'),
        'res_model': 'sale.order',
        'res_id': new_salesorder.id,
        'view_type': 'form',
        'view_mode': 'form',
        'view_id': view_id,
        'target': 'new'
        }

        return view_data