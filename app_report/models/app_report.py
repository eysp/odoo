# from odoo import models, fields, api



# class SaleOrder_Data(models.Model):
#     _inherit = 'sale.order'

#     channel_order_number = fields.Char(string = 'Channel Order')
#     payment_type = fields.Char(string = 'Payment Type')
#     description_1 = fields.Char(string = 'Description 1')
#     dealer_discount = fields.Char(string = 'Dealer Discount1')
#     check_it = fields.Boolean(string = 'check it', help= 'this is just to test booleean field')
#     result = fields.Float(string='result', digits=(12,6))
    
    


#     def _prepare_invoice(self):
        
#         self.ensure_one()
#         journal = self.env['account.move'].with_context(default_move_type='out_invoice')._get_default_journal()
#         if not journal:
#             raise UserError(('Please define  accounting sales journal for the company %s (%s).') % (self.company_id.name, self.company_id.id))

#         invoice_vals = {
#             'ref': self.client_order_ref or '',
#             'move_type': 'out_invoice',
#             'narration': self.note,
#             'currency_id': self.pricelist_id.currency_id.id,
#             'campaign_id': self.campaign_id.id,
#             'medium_id': self.medium_id.id,
#             'source_id': self.source_id.id,
#             'invoice_user_id': self.user_id and self.user_id.id,
#             'team_id': self.team_id.id,
#             'channel_order_number':self.channel_order_number,
#             'partner_id': self.partner_invoice_id.id,
#             'partner_shipping_id': self.partner_shipping_id.id,
#             'fiscal_position_id': (self.fiscal_position_id or self.fiscal_position_id.get_fiscal_position(self.partner_invoice_id.id)).id,
#             'partner_bank_id': self.company_id.partner_id.bank_ids[:1].id,
#             'journal_id': journal.id,  # company comes from the journal
#             'invoice_origin': self.name,
#             'invoice_payment_term_id': self.payment_term_id.id,
#             'payment_reference': self.reference,
#             'transaction_ids': [(6, 0, self.transaction_ids.ids)],
#             'invoice_line_ids': [],
#             'company_id': self.company_id.id,
#         }
#         return invoice_vals

#     # def create_sales_order(self):
#     #     # order_reference = self.name

#     #     #line_items_vals = []
#     #     # for line in self.line_items:
#     #     #     line_items_vals.append({
#     #     #         'product_id': line.product_id.id,
#     #     #         'name': line.name,
#     #     #         'product_uom_qty': line.product_qty,
#     #     #         'price_unit': line.price_unit,
#     #     #         'line_project_focus' : line.line_project_focus.id
#     #     #     })

#     #     vals = {
#     #           'partner_id' : self.partner_id.id, 
#     #           'payment_type':'Cash', 
#     #         # 'freight_supplier_currency' : self.freight_supplier_currency,
#     #         # 'exchange_rate' : self.supplier_client_exchange_rate,
#     #         # 'design_engineering' : self.design_engineering, 
#     #         # 'commissioning' : self.commissioning,
#     #         # 'handlings' : self.handlings,
#     #         # 'custom_value' : self.custom_value,
#     #         # 'project_focus' : self.project_focus.id,
#     #         # 'standard_sale_order' : False,
#     #         # 'order_line' : [(0, 0, invoice_line_id) for invoice_line_id in line_items_vals]
#     #     }

#     #     # print("**************************************** ******************************************")
#     #     # print(self.partner_id.id)

#     #     view_ref = self.env['ir.model.data'].get_object_reference('sale', 'view_order_form')
#     #     view_id = view_ref[1] if view_ref else False

#     #     new_salesorder = self.env['sale.order'].create(vals)
    
#     #     view_data = {
#     #     'type': 'ir.actions.act_window',
#     #     'name': ('Sales Order'),
#     #     'res_model': 'sale.order',
#     #     'res_id': new_salesorder.id,
#     #     'view_type': 'form',
#     #     'view_mode': 'form',
#     #     'view_id': view_id,
#     #     'target': 'new'
#     #     }

#     #     return view_data


#     def _prepare_invoice_line(self, **optional_values):
#         """
#         Prepare the dict of values to create the new invoice line for a sales order line.

#         :param qty: float quantity to invoice
#         :param optional_values: any parameter that should be added to the returned invoice line
#         """
#         self.ensure_one()
#         res = {
#             'display_type': self.display_type,
#             'sequence': self.sequence,
#             'name': self.name,
#             'product_id': self.product_id.id,
#             'product_uom_id': self.product_uom.id,
#             'quantity': self.qty_to_invoice,
#             'discount': self.discount,
#             'seller_discount': self.seller_discount,
#             'price_unit': self.price_unit,
#             'tax_ids': [(6, 0, self.tax_id.ids)],
#             'analytic_account_id': self.order_id.analytic_account_id.id,
#             'analytic_tag_ids': [(6, 0, self.analytic_tag_ids.ids)],
#             'sale_line_ids': [(4, self.id)],
#         }
#         if optional_values:
#             res.update(optional_values)
#         if self.display_type:
#             res['account_id'] = False
#         return res

# class Purchase(models.Model):
#     _inherit = 'Purchase.order'

#     def create_sales_order(self):
#         # order_reference = self.name

#         #line_items_vals = []
#         # for line in self.line_items:
#         #     line_items_vals.append({
#         #         'product_id': line.product_id.id,
#         #         'name': line.name,
#         #         'product_uom_qty': line.product_qty,
#         #         'price_unit': line.price_unit,
#         #         'line_project_focus' : line.line_project_focus.id
#         #     })

#         vals = {
#               'partner_id' : self.partner_id.id, 
#               'payment_type':'Cash', 
#             # 'freight_supplier_currency' : self.freight_supplier_currency,
#             # 'exchange_rate' : self.supplier_client_exchange_rate,
#             # 'design_engineering' : self.design_engineering, 
#             # 'commissioning' : self.commissioning,
#             # 'handlings' : self.handlings,
#             # 'custom_value' : self.custom_value,
#             # 'project_focus' : self.project_focus.id,
#             # 'standard_sale_order' : False,
#             # 'order_line' : [(0, 0, invoice_line_id) for invoice_line_id in line_items_vals]
#         }

#         # print("**************************************** ******************************************")
#         # print(self.partner_id.id)

#         view_ref = self.env['ir.model.data'].get_object_reference('sale', 'view_order_form')
#         view_id = view_ref[1] if view_ref else False

#         new_salesorder = self.env['sale.order'].create(vals)
    
#         view_data = {
#         'type': 'ir.actions.act_window',
#         'name': ('Sales Order'),
#         'res_model': 'sale.order',
#         'res_id': new_salesorder.id,
#         'view_type': 'form',
#         'view_mode': 'form',
#         'view_id': view_id,
#         'target': 'new'
#         }

#         return view_data

# class SaleOrderLine(models.Model):
#     _inherit = 'sale.order.line'
#     seller_discount = fields.Float(string='Seller Discount')

# class AccountMove_Data(models.Model):
#     _inherit = 'account.move'

#     # seller_discount = fields.Float(string = 'Seller Discount',readonly=True, tracking=True)

#     channel_order_number = fields.Char(string = 'Channel Order No.',readonly=True, tracking=True)
    
#     @api.depends('line_ids.price_unit', 'line_ids.seller_discount','line_ids.quantity')
#     def _cal_total_discount(self):
#         for order in self:
#             cal_discount = 0
#             for line_items in order.line_ids:
#                 cal_discount = cal_discount + (line_items.quantity * line_items.price_unit * line_items.seller_discount) / 100
#             order.calculated_discount = cal_discount
        

#     calculated_discount = fields.Float(string = 'Discount', compute = '_cal_total_discount', store = True, digits=(12,4))

#     @api.depends('amount_untaxed','calculated_discount')
#     def _cal_grand_total(self):
#         for order in self:
#             order.grand_total = order.amount_untaxed + order.calculated_discount

#     grand_total = fields.Float(string = 'Grand Total', store = True, compute = '_cal_grand_total')

#     @api.depends('calculated_discount', 'grand_total')
#     def _cal_total_baht_escl_vat(self):
#         for orders in self:
#             orders.total_baht_excl_VAT = orders.grand_total - orders.calculated_discount

#     total_baht_excl_VAT = fields.Float(string = 'Total Baht Excl VAT', compute = '_cal_total_baht_escl_vat', store= True, digits=(12,4))

#     @api.depends('total_baht_excl_VAT')
#     def _cal_total_baht_incl_vat(self):
#         for orders in self:
#             orders.total_baht_incl_VAT = orders.total_baht_excl_VAT * 1.07

#     total_baht_incl_VAT = fields.Float(string = 'Total Baht Incl VAT', compute = '_cal_total_baht_incl_vat', store = True, digits=(12,4))

#     @api.depends('total_baht_excl_VAT','total_baht_incl_VAT')
#     def _cal_total_vat(self):
#         for orders in self:
#             orders.vat = orders.total_baht_incl_VAT - orders.total_baht_excl_VAT

#     vat = fields.Float(string = 'Vat', compute = '_cal_total_vat', store = True, digits=(12,4))

    



# class AccountMove_Line_Data(models.Model):
#     _inherit = 'account.move.line'
#     seller_discount = fields.Float('seller_discount')

#--------------------------------------------------------------
# import the files

# from odoo import api, fields, models


# class QuoteCalculator_purchase(models.Model):
#     _inherit = 'purchase.order'
#     dealer_discount = fields.Float(string = 'Dealer Discount', digits = (12, 4))
#     freight_supplier_currency = fields.Float(string = 'Freight Supplier Currency')
#     supplier_client_exchange_rate = fields.Float(string = 'Supplier/Client Exchange Rate', digits = (12, 4))
#     commissioning = fields.Float(string = 'Commissioning')	
#     design_engineering = fields.Float(string = 'Design Engineering')
#     handlings = fields.Float(string = 'Handling')
#     custom_value = fields.Float(string = 'Customs')
#     line_items = fields.One2many('purchase.order.line', 'order_id', string='Order Line Items')
#     dealer_price = fields.Float(string='Purchase Price', compute = '_calPrice', store = True)
#     project = fields.Many2one('project.project',string='Project')
#     project_focus = fields.Many2one('focus_areas', string='Focus Area')

#     @api.depends('line_items.price_total','freight_supplier_currency', 'project_focus', 'commissioning', 'design_engineering','handlings','custom_value')
#     def _amount_all(self):
#         for order in self:
#             amount_untaxed = amount_tax = 0.0
#             other_amount = order.freight_supplier_currency + order.commissioning + order.design_engineering + order.handlings + order.custom_value

#             project = order.project_focus

#             for line in order.order_line:
#                 line._compute_amount()
#                 amount_untaxed += line.price_subtotal
#                 amount_tax += line.price_tax

#                 # this part will add project into line items
#                 if not line.line_project_focus:
#                     line.line_project_focus = project

#             order.update({
#                 'amount_untaxed': order.currency_id.round(amount_untaxed),
#                 'amount_tax': order.currency_id.round(amount_tax),
#                 'amount_total': amount_untaxed + amount_tax + other_amount,
#             })

#     # to only pass the field values in purchase order line
#     @api.depends('dealer_discount','project_focus')
#     def _calPrice(self):
#         for orderitems in self:
#             discount = orderitems.dealer_discount
#             # sel_project = orderitems.project
#             sel_project_focus = orderitems.project_focus
#             for line in orderitems.line_items:
#                 line.line_dealer_discount = discount
#                 # line.line_project = sel_project
#                 if not line.line_project_focus:
#                     line.line_project_focus = sel_project_focus

#     @api.onchange('dealer_discount')
#     def _onchange_dealer_discount(self):
#         for orders in self:
#             discount = orders.dealer_discount
#             for line in orders.line_items:
#                 line.line_dealer_discount = discount

#     @api.onchange('project_focus')
#     def _onchange_project_focus(self):
#         for order in self:
#             project = order.project_focus
#             for line in order.line_items:
#                 if not line.line_project_focus:
#                     line.line_project_focus = project
    
#     # update the data in the report
#     def update_line_data(self):
#         for orders in self:
#             discount = orders.dealer_discount
#             # sel_project = orders.project
#             sel_project_focus = orders.project_focus
#             for line in orders.line_items:
#                 line.line_dealer_discount = discount
#                 # line.line_project = sel_project
#                 if not line.line_project_focus:
#                     line.line_project_focus = sel_project_focus

    
#     # create button "Create Sales Order" in Purchase
#     def create_sales_order(self):
#         # order_reference = self.name

#         line_items_vals = []
#         for line in self.line_items:
#             line_items_vals.append({
#                 'product_id': line.product_id.id,
#                 'name': line.name,
#                 'product_uom_qty': line.product_qty,
#                 'price_unit': line.price_unit,
#                 'line_project_focus' : line.line_project_focus.id
#             })

#         vals = {
#             'partner_id' : self.partner_id.id,  
#             'freight_supplier_currency' : self.freight_supplier_currency,
#             'exchange_rate' : self.supplier_client_exchange_rate,
#             'design_engineering' : self.design_engineering, 
#             'commissioning' : self.commissioning,
#             'handlings' : self.handlings,
#             'custom_value' : self.custom_value,
#             'project_focus' : self.project_focus.id,
#             'standard_sale_order' : False,
#             'order_line' : [(0, 0, invoice_line_id) for invoice_line_id in line_items_vals]
#         }

#         # print("**************************************** ******************************************")
#         # print(self.partner_id.id)

#         view_ref = self.env['ir.model.data'].get_object_reference('sale', 'view_order_form')
#         view_id = view_ref[1] if view_ref else False

#         new_salesorder = self.env['sale.order'].create(vals)
    
#         view_data = {
#         'type': 'ir.actions.act_window',
#         'name': ('Sales Order'),
#         'res_model': 'sale.order',
#         'res_id': new_salesorder.id,
#         'view_type': 'form',
#         'view_mode': 'form',
#         'view_id': view_id,
#         'target': 'new'
#         }

#         return view_data

#     def _prepare_invoice(self):
#         """Prepare the dict of values to create the new invoice for a purchase order.
#         """
#         self.ensure_one()
#         move_type = self._context.get('default_move_type', 'in_invoice')
#         journal = self.env['account.move'].with_context(default_move_type=move_type)._get_default_journal()
#         if not journal:
#             raise UserError(_('Please define an accounting purchase journal for the company %s (%s).') % (self.company_id.name, self.company_id.id))

#         partner_invoice_id = self.partner_id.address_get(['invoice'])['invoice']
#         invoice_vals = {
#             'ref': self.partner_ref or '',
#             'move_type': move_type,
#             'narration': self.notes,
#             'project' : self.project_focus,
#             'currency_id': self.currency_id.id,
#             'invoice_user_id': self.user_id and self.user_id.id,
#             'partner_id': partner_invoice_id,
#             'fiscal_position_id': (self.fiscal_position_id or self.fiscal_position_id.get_fiscal_position(partner_invoice_id)).id,
#             'payment_reference': self.partner_ref or '',
#             'partner_bank_id': self.partner_id.bank_ids[:1].id,
#             'invoice_origin': self.name,
#             'invoice_payment_term_id': self.payment_term_id.id,
#             'invoice_line_ids': [],
#             'company_id': self.company_id.id,
#             'freight_supplier_currency' : self.freight_supplier_currency,
#             'commissioning' : self.commissioning,
#             'design_engineering' : self.design_engineering,
#             'handlings' : self.handlings,
#             'customs' : self.custom_value,
#             'is_bill' : True,
#         }
#         return invoice_vals

# class QuoteCalculator_purchase_order_line(models.Model):
#     _inherit = 'purchase.order.line'
#     dealer_purchase_price = fields.Float(string='Dealer Purchase Price', compute= '_cal_price')
#     line_dealer_discount = fields.Float(string = 'Dealer Discount')
#     line_project = fields.Many2one('project.project',string='Project')
#     line_project_focus = fields.Many2one('focus_areas',string='Focus Area')

#     @api.onchange('line_dealer_discount','price_unit')
#     @api.depends('price_unit', 'line_dealer_discount')
#     def _cal_price(self):
#         for line in self:
#             line.dealer_purchase_price = line.price_unit*(1 - line.line_dealer_discount)



#     @api.depends('product_qty', 'price_unit', 'taxes_id','dealer_purchase_price')
#     def _compute_amount(self):
#         for line in self:
#             vals = line._prepare_compute_all_values()
#             dealer_price = line.dealer_purchase_price
#             taxes = line.taxes_id.compute_all(
#                 dealer_price,
#                 vals['currency_id'],
#                 vals['product_qty'],
#                 vals['product'],
#                 vals['partner'])
#             line.update({
#                 'price_tax': sum(t.get('amount', 0.0) for t in taxes.get('taxes', [])),
#                 'price_total': taxes['total_included'],
#                 'price_subtotal': taxes['total_excluded'],
#             })

#     def _prepare_account_move_line(self, move=False):
#         self.ensure_one()
#         res = {
#             'display_type': self.display_type,
#             'sequence': self.sequence,
#             'name': '%s: %s' % (self.order_id.name, self.name),
#             'product_id': self.product_id.id,
#             'product_uom_id': self.product_uom.id,
#             'quantity': self.qty_to_invoice,
#             'price_unit': self.dealer_purchase_price,
#             'tax_ids': [(6, 0, self.taxes_id.ids)],
#             'analytic_account_id': self.account_analytic_id.id,
#             'analytic_tag_ids': [(6, 0, self.analytic_tag_ids.ids)],
#             'purchase_line_id': self.id,
#         }
#         if not move:
#             return res

#         if self.currency_id == move.company_id.currency_id:
#             currency = False
#         else:
#             currency = move.currency_id

#         res.update({
#             'move_id': move.id,
#             'currency_id': currency and currency.id or False,
#             'date_maturity': move.invoice_date_due,
#             'partner_id': move.partner_id.id,
#         })
#         return res


# class QuoteCalculator_SalesOrder(models.Model):
#     _inherit = "sale.order"
#     _description = "Sale Order"

#     standard_sale_order = fields.Boolean(string = 'Standard Sale Order', default=True)
#     margin = fields.Float(string = 'Margin')

#     freight = fields.Float(string = 'Freight')
#     aud_freight = fields.Float(string = 'Freight Value', compute = '_cal_Freight_Value', store = True)
#     exchange_rate = fields.Float(string ='Exchange Rate', digits = (12, 4))
#     cost_aud_per_unit = fields.Float(string = 'Cost AUD per Unit', compute ='_calCost', store =True)
#     line_items = fields.One2many('sale.order.line', 'order_id', string='Order Lines Items')

#     design_engineering = fields.Float(string = 'Design Engineering Value')
#     margin_supply_charges = fields.Float(string = 'Margin Supply Charges')
#     commissioning = fields.Float(string = 'Commissioning')	
#     freight_supplier_currency = fields.Float(string = 'Freight Supplier Currency')
#     handlings = fields.Float(string = 'Handling')
#     custom_value = fields.Float(string = 'Customs')
#     project = fields.Many2one('project.project',string='Project')
#     project_focus = fields.Many2one('focus_areas', string='Focus Area')
    

#     # @api.onchange('standard_sale_order')
#     # def _onchange_standard_sale_order(self):
#     #     for order in self:
#     #         is_saleorder = order.standard_sale_order
#     #         for line in order.line_items:
#     #             line.standard_sale_order = is_saleorder

#     @api.onchange('project_focus')
#     def _onchange_project_focus(self):
#         for order in self:
#             sel_project_focus = order.project_focus
#             for line in order.line_items:
#                 if not line.line_project_focus:
#                     line.line_project_focus = sel_project_focus


#     @api.depends('exchange_rate', 'margin', 'freight','standard_sale_order')
#     def _cal_Freight_Value(self):
#         for order in self:
#             exc_rate = order.exchange_rate
#             margin_val = order.margin
#             freight_val = order.freight
#             cal_freight_value = 0
#             if not order.standard_sale_order:
#                 for line in order.line_items:
#                     exchange_rate = 1/(exc_rate - 0.005)
#                     cal_freight_value = cal_freight_value + (line.price_unit * exchange_rate * (1 + margin_val)) * freight_val
#                 order.aud_freight = cal_freight_value

                


#     @api.depends('design_engineering','margin_supply_charges', 'exchange_rate','standard_sale_order')
#     def _cal_design_engineering(self):
#         for orders in self:
#             orders.calculated_design_engineering = (orders.design_engineering * (1 + orders.margin_supply_charges) * (1/(orders.exchange_rate - 0.005)))

#     calculated_design_engineering = fields.Float(string = 'Design Engineering', compute = '_cal_design_engineering', store = True)

#     @api.depends('freight_supplier_currency','margin_supply_charges', 'exchange_rate','standard_sale_order')
#     def _cal_freight_supplier_currency(self):
#         for orders in self:
#             orders.calculated_freight_supplier_currency = (orders.freight_supplier_currency * (1 + orders.margin_supply_charges) * (1/(orders.exchange_rate - 0.005)))

#     calculated_freight_supplier_currency = fields.Float(string = 'Freight Supplier Currency', compute = '_cal_freight_supplier_currency', store = True)

#     @api.depends('commissioning','margin_supply_charges', 'exchange_rate','standard_sale_order')
#     def _cal_commissioning(self):
#         for orders in self:
#             orders.calculated_commissioning = (orders.commissioning * (1 + orders.margin_supply_charges) * (1/(orders.exchange_rate - 0.005)))

#     calculated_commissioning = fields.Float(string = 'Commissioning', compute = '_cal_commissioning', store = True)

#     @api.depends('handlings','margin_supply_charges', 'exchange_rate','standard_sale_order')
#     def _cal_handlings(self):
#         for orders in self:
#             orders.calculated_handlings = (orders.handlings * (1 + orders.margin_supply_charges) * (1/(orders.exchange_rate - 0.005)))

#     calculated_handlings = fields.Float(string = 'Handling', compute = '_cal_handlings', store = True)

#     @api.depends('custom_value','margin_supply_charges', 'exchange_rate','standard_sale_order')
#     def _cal_custom_value(self):
#         for orders in self:
#             orders.calculated_custom_value = (orders.custom_value * (1 + orders.margin_supply_charges) * (1/(orders.exchange_rate - 0.005)))

#     calculated_custom_value = fields.Float(string = 'Customs', compute = '_cal_custom_value', store = True)


#     margin_local_charges = fields.Float(string = 'Margin Local Charges')

#     local_customs_value = fields.Float(string = 'Local Customs')
#     local_customs_margin_value = fields.Float(string = 'Local Customs', compute = '_cal_margin_value')

#     destination_charges = fields.Float(string = 'Destination Charges')
#     destination_margin_charges = fields.Float(string = 'Destination Charges', compute = '_cal_margin_value')

#     local_freight = fields.Float(string = 'Local Freight')
#     local_freight_margin = fields.Float(string = 'Local Freight', compute = '_cal_margin_value')

#     local_commissioning = fields.Float(string = 'Local Commissioning')
#     local_commissioning_margin = fields.Float(string = 'Local Commissioning', compute = '_cal_margin_value')


#     retail_discount = fields.Float(string='Retail Discount')

#     @api.depends('amount_untaxed', 'retail_discount','standard_sale_order')
#     def _cal_retail_discount(self):
#         for orders in self:
#             orders.computed_retail_discount = (-1 * orders.amount_untaxed * orders.retail_discount)
    
#     computed_retail_discount = fields.Float(string='Retail Discount', compute = '_cal_retail_discount', store = True) 

       
    
#     @api.depends('amount_total')
#     def _calGst(self):
#         for orders in self:
#             orders.gst_value = orders.amount_total * 0.1
    
#     gst_value = fields.Float(string='GST', compute = '_calGst' , store = True)

#     @api.depends('line_items.aud_total')
#     def _cal_subtotal(self):
#         for orders in self:
#             subtotal = 0
#             for line in orders.line_items:
#                 subtotal = subtotal + line.aud_total
#             orders.subtotal_value = subtotal

#     subtotal_value = fields.Float(string = 'Sub Total with AUD', compute = '_cal_subtotal', store = True)

#     # @api.depends('line_items', 'local_freight', 'local_customs_value', 'destination_charges', 'margin_local_charges', 'local_commissioning','standard_sale_order')
#     # def _calLocal_destintaion_charges(self):
#     #     for orders in self:
#     #         margin_local_charges = orders.margin_local_charges
#     #         local_freight = orders.local_freight
#     #         local_customs_value = orders.local_customs_value
#     #         destination_charges = orders.destination_charges
#     #         local_commissioning = orders.local_commissioning
#     #         orders.local_destination_charges = (local_freight + local_customs_value + destination_charges + local_commissioning) *  (1 + margin_local_charges)

#     # local_destination_charges = fields.Float(string = 'LOCAL DESTINATION CHARGES', compute = '_calLocal_destintaion_charges', store = True)

#     @api.depends('local_freight', 'local_customs_value', 'destination_charges', 'margin_local_charges', 'local_commissioning','standard_sale_order')
#     def _cal_margin_value(self):
#         for order in self:
#             order.local_customs_margin_value = order.local_customs_value * (1 + order.margin_local_charges)
#             order.destination_margin_charges = order.destination_charges * (1 + order.margin_local_charges)
#             order.local_freight_margin = order.local_freight * (1 + order.margin_local_charges)
#             order.local_commissioning_margin = order.local_commissioning * (1 + order.margin_local_charges)


#     @api.depends('computed_retail_discount','calculated_freight_supplier_currency','calculated_design_engineering','calculated_commissioning', 'calculated_custom_value', 'amount_untaxed','standard_sale_order')
#     def _cal_shipping_insurance(self):
#         for orders in self:
#             # orders.shipping_insurance = (
#             # orders.subtotal_value + (-1 * (orders.subtotal_value * orders.retail_discount)) +
#             # (orders.freight_supplier_currency * (1 + orders.margin_supply_charges))/(orders.exchange_rate - 0.005) + 
#             # (orders.handlings * (1 + orders.margin_supply_charges))/(orders.exchange_rate - 0.005) +
#             # (orders.design_engineering * (1 + orders.margin_supply_charges))/(orders.exchange_rate - 0.005) + 
#             # (orders.commissioning * (1 + orders.margin_supply_charges))/(orders.exchange_rate - 0.005) ) * 0.005
#             orders.shipping_insurance = (orders.amount_untaxed + orders.computed_retail_discount + orders.calculated_freight_supplier_currency + orders.calculated_design_engineering + orders.calculated_commissioning  + orders.calculated_custom_value)*0.005 

#     shipping_insurance = fields.Float(string = 'Shipping Insurance', compute = '_cal_shipping_insurance', store = True)
    
#     @api.depends('line_items.price_total', 'computed_retail_discount','calculated_freight_supplier_currency','calculated_commissioning','local_customs_margin_value','destination_margin_charges','local_freight_margin','local_commissioning_margin','calculated_handlings','shipping_insurance','calculated_design_engineering','calculated_custom_value','standard_sale_order', 'project_focus')
#     def _amount_all(self):
#         """
#         Compute the total amounts of the SO.
#         """

#         """
#         Also add the project into line items, this is the method which will be executed everytime
#         """
#         for order in self:
#             amount_untaxed = amount_tax = 0.0
#             other_amount = 0
#             project = order.project_focus


#             if order.standard_sale_order:
#                 for line in order.order_line:
#                     amount_untaxed += line.price_subtotal
#                     amount_tax += line.price_tax
                   
#                    # this part will add project into line items
#                     if not line.line_project_focus:
#                         line.line_project_focus = project

#                 order.update({
#                     'amount_untaxed': amount_untaxed,
#                     'amount_tax': amount_tax,
#                     'amount_total': amount_untaxed + amount_tax,
#                 })
#             else:
#                 other_amount = order.computed_retail_discount + order.calculated_freight_supplier_currency + order.calculated_commissioning + order.calculated_design_engineering + order.calculated_handlings + order.calculated_custom_value + order.shipping_insurance + order.local_customs_margin_value + order.destination_margin_charges + order.local_freight_margin + order.local_commissioning_margin
#                 for line in order.order_line:
#                     amount_untaxed += line.price_subtotal
#                     amount_tax += line.price_tax

#                     # this part will add project into line items
#                     if not line.line_project_focus:
#                         line.line_project_focus = project

#                 order.update({
#                     'amount_untaxed': amount_untaxed,
#                     'amount_tax': amount_tax,
#                     'amount_total': amount_untaxed + other_amount,
#                 })

#     @api.depends('amount_total','gst_value')
#     def _cal_total_ince_gst(self):
#         for orders in self:
#             orders.total_inc_gst = orders.amount_total + orders.gst_value

#     total_inc_gst = fields.Float(string = 'Total Inc GST', compute = '_cal_total_ince_gst', store = True)

#     @api.depends('line_items','exchange_rate','margin','freight','standard_sale_order')
#     def _calCost(self):
#         for orderitems in self:
#             exc = 0
#             #cost_aud_per_unit_val = 0
#             exc_rate = orderitems.exchange_rate
#             margin_val = orderitems.margin
#             freight_val = orderitems.freight
#             sel_project_focus = orderitems.project_focus
#             if not orderitems.standard_sale_order:
#                 for line in orderitems.line_items:
#                     EXC = 1/(exc_rate - 0.005)
#                     cost_aud_per_unit_val = line.cost_aud_per_unit1 = EXC * line.price_unit
#                     aud_marginvalue = line.aud_unit_price_with_margin = cost_aud_per_unit_val * (1 + margin_val)
#                     aud_freight = (line.price_unit * EXC * (1 + margin_val)) * freight_val
#                     aud_per_unit = line.aud_unit_total = aud_marginvalue + aud_freight
#                     line.aud_total = aud_per_unit * line.product_uom_qty
#             else:
#                 for line in orderitems.line_items:
#                     line.aud_unit_total = line.price_unit
#                     if not line.line_project_focus:
#                         line.line_project_focus = sel_project_focus

#     def _prepare_invoice(self):
#         """
#         Prepare the dict of values to create the new invoice for a sales order. This method may be
#         overridden to implement custom invoice generation (making sure to call super() to establish
#         a clean extension chain).
#         """
#         self.ensure_one()
#         journal = self.env['account.move'].with_context(default_move_type='out_invoice')._get_default_journal()
#         if not journal:
#             raise UserError(_('Please define an accounting sales journal for the company %s (%s).') % (self.company_id.name, self.company_id.id))
#         if self.standard_sale_order:
#             invoice_vals = {
#                 'ref': self.client_order_ref or '',
#                 'move_type': 'out_invoice',
#                 'narration': self.note,
#                 'project': self.project_focus,
#                 'currency_id': self.pricelist_id.currency_id.id,
#                 'campaign_id': self.campaign_id.id,
#                 'medium_id': self.medium_id.id,
#                 'source_id': self.source_id.id,
#                 'invoice_user_id': self.user_id and self.user_id.id,
#                 'team_id': self.team_id.id,
#                 'partner_id': self.partner_invoice_id.id,
#                 'partner_shipping_id': self.partner_shipping_id.id,
#                 'fiscal_position_id': (self.fiscal_position_id or self.fiscal_position_id.get_fiscal_position(self.partner_invoice_id.id)).id,
#                 'partner_bank_id': self.company_id.partner_id.bank_ids[:1].id,
#                 'journal_id': journal.id,  # company comes from the journal
#                 'invoice_origin': self.name,
#                 'invoice_payment_term_id': self.payment_term_id.id,
#                 'payment_reference': self.reference,
#                 'transaction_ids': [(6, 0, self.transaction_ids.ids)],
#                 'invoice_line_ids': [],
#                 'company_id': self.company_id.id,
#                 'standard_sale_order' : self.standard_sale_order,
#             }
#         else:
#              invoice_vals = {
#                 'ref': self.client_order_ref or '',
#                 'move_type': 'out_invoice',
#                 'narration': self.note,
#                 'project': self.project_focus,
#                 'currency_id': self.pricelist_id.currency_id.id,
#                 'campaign_id': self.campaign_id.id,
#                 'medium_id': self.medium_id.id,
#                 'source_id': self.source_id.id,
#                 'invoice_user_id': self.user_id and self.user_id.id,
#                 'team_id': self.team_id.id,
#                 'partner_id': self.partner_invoice_id.id,
#                 'partner_shipping_id': self.partner_shipping_id.id,
#                 'fiscal_position_id': (self.fiscal_position_id or self.fiscal_position_id.get_fiscal_position(self.partner_invoice_id.id)).id,
#                 'partner_bank_id': self.company_id.partner_id.bank_ids[:1].id,
#                 'journal_id': journal.id,  # company comes from the journal
#                 'invoice_origin': self.name,
#                 'invoice_payment_term_id': self.payment_term_id.id,
#                 'payment_reference': self.reference,
#                 'transaction_ids': [(6, 0, self.transaction_ids.ids)],
#                 'invoice_line_ids': [],
#                 'company_id': self.company_id.id,
#                 'standard_sale_order' : self.standard_sale_order,
#                 'freight_supplier_currency' : self.calculated_freight_supplier_currency,
#                 'commissioning' : self.calculated_commissioning,
#                 'design_engineering' : self.calculated_design_engineering,
#                 'handlings' : self.calculated_handlings,
#                 'customs' : self.calculated_custom_value,
#                 'retail_discount' : self.computed_retail_discount,
#                 'shipping_insurance' : self.shipping_insurance,
#                 'local_customs_value' : self.local_customs_margin_value,
#                 'destination_charges' : self.destination_margin_charges,
#                 'local_freight' : self.local_freight_margin,
#                 'local_commissioning' : self.local_commissioning_margin,
#                 'gst' : self.gst_value,
#                 'total_inc_gst' : self.total_inc_gst,
#                 'total_exc_gst' : self.amount_total,    
#             }

#         return invoice_vals


    
    

# class QuoteCalculator_SalesOrderLine(models.Model):
#     _inherit = "sale.order.line"
#     cost_aud_per_unit1 = fields.Float(string = 'Cost AUD per Unit')
#     aud_unit_price_with_margin = fields.Float(string = 'AUD Unit PRICE with Margin')
#     aud_per_unit = fields.Float(string = 'AUD per UNIT')
#     aud_unit_total = fields.Float(string = 'AUD UNIT TOTAL')
#     aud_total = fields.Float(string = 'AUD TOTAL')
#     line_project_focus = fields.Many2one('focus_areas',string='Focus Area')
#     standard_sale_order = fields.Boolean(string = 'Standard Sales Order')

#     @api.depends('product_uom_qty', 'discount', 'aud_unit_total', 'tax_id')
#     def _compute_amount(self):
#         for line in self:
#             price = line.aud_unit_total * (1 - (line.discount or 0.0) / 100.0)

#             taxes = line.tax_id.compute_all(price, line.order_id.currency_id, line.product_uom_qty, product=line.product_id, partner=line.order_id.partner_shipping_id)
#             line.update({
#                 'price_tax': sum(t.get('amount', 0.0) for t in taxes.get('taxes', [])),
#                 'price_total': taxes['total_included'],
#                 'price_subtotal': taxes['total_excluded'],
#             })
#             if self.env.context.get('import_file', False) and not self.env.user.user_has_groups('account.group_account_manager'):
#                 line.tax_id.invalidate_cache(['invoice_repartition_line_ids'], [line.tax_id.id])

#     def _prepare_invoice_line(self, **optional_values):
#         """
#         Prepare the dict of values to create the new invoice line for a sales order line.

#         :param qty: float quantity to invoice
#         :param optional_values: any parameter that should be added to the returned invoice line
#         """
#         self.ensure_one()

#         if self.is_downpayment:
#             unit_price = self.price_unit
#         else:
#             unit_price = self.aud_unit_total
        
        
#         if self.order_id.standard_sale_order:
#             id = self.tax_id.ids
#         else:
#             tax = self.env['account.tax'].search([('name', '=', 'BAS Excluded (Sales)')], limit=1)
#             id = tax.ids

#         res = {
#             'display_type': self.display_type,
#             'sequence': self.sequence,
#             'name': self.name,
#             'product_id': self.product_id.id,
#             'product_uom_id': self.product_uom.id,
#             'quantity': self.qty_to_invoice,
#             'discount': self.discount,
#             'price_unit': unit_price,
#             'tax_ids': [(6, 0, id)],
#             'analytic_account_id': self.order_id.analytic_account_id.id,
#             'analytic_tag_ids': [(6, 0, self.analytic_tag_ids.ids)],
#             'sale_line_ids': [(4, self.id)],
#             'is_downpayment':self.is_downpayment, 
#         }
#         if optional_values:
#             res.update(optional_values)
#         if self.display_type:
#             res['account_id'] = False
#         return res

# class QuoteCalculator_Sale_Advance_Payment(models.TransientModel):
#     _inherit = "sale.advance.payment.inv"

#     def _get_advance_details(self, order):
#         if self.advance_payment_method == 'percentage':
#             if order.standard_sale_order:
#                 amount = order.amount_untaxed * self.amount / 100
#             else:
#                 amount = order.total_inc_gst * self.amount / 100
#             name = ("Down payment of %s%%") % (self.amount)
#         else:
#             amount = self.fixed_amount
#             name = ('Down Payment')

#         return amount, name
    
#     def _prepare_invoice_values(self, order, name, amount, so_line):

#         if order.standard_sale_order:
#             id = so_line.tax_id.ids
#         else:
#             tax = self.env['account.tax'].search([('name', '=', 'BAS Excluded (Sales)')], limit=1)
#             id = tax.ids

#         invoice_vals = {
#             'ref': order.client_order_ref,
#             'move_type': 'out_invoice',
#             'invoice_origin': order.name,
#             'invoice_user_id': order.user_id.id,
#             'narration': order.note,
#             'partner_id': order.partner_invoice_id.id,
#             'fiscal_position_id': (order.fiscal_position_id or order.fiscal_position_id.get_fiscal_position(order.partner_id.id)).id,
#             'partner_shipping_id': order.partner_shipping_id.id,
#             'currency_id': order.pricelist_id.currency_id.id,
#             'payment_reference': order.reference,
#             'invoice_payment_term_id': order.payment_term_id.id,
#             'partner_bank_id': order.company_id.partner_id.bank_ids[:1].id,
#             'team_id': order.team_id.id,
#             'campaign_id': order.campaign_id.id,
#             'medium_id': order.medium_id.id,
#             'source_id': order.source_id.id,
#             'invoice_line_ids': [(0, 0, {
#                 'name': name,
#                 'price_unit': amount,
#                 'quantity': 1.0,
#                 'product_id': self.product_id.id,
#                 'product_uom_id': so_line.product_uom.id,
#                 'tax_ids': [(6, 0, id)],
#                 'sale_line_ids': [(6, 0, [so_line.id])],
#                 'analytic_tag_ids': [(6, 0, so_line.analytic_tag_ids.ids)],
#                 'analytic_account_id': order.analytic_account_id.id or False,
#             })],
#         }

#         return invoice_vals


# class Quote_Calculator_Focuses_Area(models.Model):
#         _name='focus_areas'
#         _inherit = ['mail.thread','mail.activity.mixin']
#         name = fields.Char(string = 'Name', store=True, tracking=True)
#         focus_area_number = fields.Char(string = 'Focus Area Number', store= True, tracking=True)
#         project = fields.Many2one('project.project', string = 'Project', tracking=True)
#         vendor = fields.Many2one('res.partner', string='Vendor', tracking=True)
#         active = fields.Boolean(string = 'Active', default = True, tracking=True)


# class QuoteCalculator_Account_Move(models.Model):
#     _inherit = "account.move"
#     project = fields.Many2one('focus_areas', string='Focus Area')



			
			


    
