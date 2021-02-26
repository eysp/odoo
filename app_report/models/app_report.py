from odoo import models, fields, api



class SaleOrder_Data(models.Model):
    _inherit = 'sale.order'

    channel_order_number = fields.Char(string = 'Channel Order')
    payment_type = fields.Char(string = 'Payment Type')
    description_1 = fields.Char(string = 'Description 1')
    dealer_discount = fields.Char(string = 'Dealer Discount1')
    check_it = fields.Boolean(string = 'check it', help= 'this is just to test booleean field')
    result = fields.Float(string='result' digits=(12,4))
    
    


    def _prepare_invoice(self):
        
        self.ensure_one()
        journal = self.env['account.move'].with_context(default_move_type='out_invoice')._get_default_journal()
        if not journal:
            raise UserError(('Please define  accounting sales journal for the company %s (%s).') % (self.company_id.name, self.company_id.id))

        invoice_vals = {
            'ref': self.client_order_ref or '',
            'move_type': 'out_invoice',
            'narration': self.note,
            'currency_id': self.pricelist_id.currency_id.id,
            'campaign_id': self.campaign_id.id,
            'medium_id': self.medium_id.id,
            'source_id': self.source_id.id,
            'invoice_user_id': self.user_id and self.user_id.id,
            'team_id': self.team_id.id,
            'channel_order_number':self.channel_order_number,
            'partner_id': self.partner_invoice_id.id,
            'partner_shipping_id': self.partner_shipping_id.id,
            'fiscal_position_id': (self.fiscal_position_id or self.fiscal_position_id.get_fiscal_position(self.partner_invoice_id.id)).id,
            'partner_bank_id': self.company_id.partner_id.bank_ids[:1].id,
            'journal_id': journal.id,  # company comes from the journal
            'invoice_origin': self.name,
            'invoice_payment_term_id': self.payment_term_id.id,
            'payment_reference': self.reference,
            'transaction_ids': [(6, 0, self.transaction_ids.ids)],
            'invoice_line_ids': [],
            'company_id': self.company_id.id,
        }
        return invoice_vals

    def create_sales_order(self):
        # order_reference = self.name

        #line_items_vals = []
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
              'payment_type':'Cash', 
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

        # print("**************************************** ******************************************")
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


    def _prepare_invoice_line(self, **optional_values):
        """
        Prepare the dict of values to create the new invoice line for a sales order line.

        :param qty: float quantity to invoice
        :param optional_values: any parameter that should be added to the returned invoice line
        """
        self.ensure_one()
        res = {
            'display_type': self.display_type,
            'sequence': self.sequence,
            'name': self.name,
            'product_id': self.product_id.id,
            'product_uom_id': self.product_uom.id,
            'quantity': self.qty_to_invoice,
            'discount': self.discount,
            'seller_discount': self.seller_discount,
            'price_unit': self.price_unit,
            'tax_ids': [(6, 0, self.tax_id.ids)],
            'analytic_account_id': self.order_id.analytic_account_id.id,
            'analytic_tag_ids': [(6, 0, self.analytic_tag_ids.ids)],
            'sale_line_ids': [(4, self.id)],
        }
        if optional_values:
            res.update(optional_values)
        if self.display_type:
            res['account_id'] = False
        return res

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'
    seller_discount = fields.Float(string='Seller Discount')

class AccountMove_Data(models.Model):
    _inherit = 'account.move'

    # seller_discount = fields.Float(string = 'Seller Discount',readonly=True, tracking=True)

    channel_order_number = fields.Char(string = 'Channel Order No.',readonly=True, tracking=True)
    
    @api.depends('line_ids.price_unit', 'line_ids.seller_discount','line_ids.quantity')
    def _cal_total_discount(self):
        for order in self:
            cal_discount = 0
            for line_items in order.line_ids:
                cal_discount = cal_discount + (line_items.quantity * line_items.price_unit * line_items.seller_discount) / 100
            order.calculated_discount = cal_discount
        

    calculated_discount = fields.Float(string = 'Discount', compute = '_cal_total_discount', store = True, digits=(12,4))

    @api.depends('amount_untaxed','calculated_discount')
    def _cal_grand_total(self):
        for order in self:
            order.grand_total = order.amount_untaxed + order.calculated_discount

    grand_total = fields.Float(string = 'Grand Total', store = True, compute = '_cal_grand_total')

    @api.depends('calculated_discount', 'grand_total')
    def _cal_total_baht_escl_vat(self):
        for orders in self:
            orders.total_baht_excl_VAT = orders.grand_total - orders.calculated_discount

    total_baht_excl_VAT = fields.Float(string = 'Total Baht Excl VAT', compute = '_cal_total_baht_escl_vat', store= True, digits=(12,4))

    @api.depends('total_baht_excl_VAT')
    def _cal_total_baht_incl_vat(self):
        for orders in self:
            orders.total_baht_incl_VAT = orders.total_baht_excl_VAT * 1.07

    total_baht_incl_VAT = fields.Float(string = 'Total Baht Incl VAT', compute = '_cal_total_baht_incl_vat', store = True, digits=(12,4))

    @api.depends('total_baht_excl_VAT','total_baht_incl_VAT')
    def _cal_total_vat(self):
        for orders in self:
            orders.vat = orders.total_baht_incl_VAT - orders.total_baht_excl_VAT

    vat = fields.Float(string = 'Vat', compute = '_cal_total_vat', store = True, digits=(12,4))

    



class AccountMove_Line_Data(models.Model):
    _inherit = 'account.move.line'
    seller_discount = fields.Float('seller_discount')

