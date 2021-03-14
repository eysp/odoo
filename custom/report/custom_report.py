from odoo import tools
from odoo import api, fields, models


class SaleReport(models.Model):
    _inherit = "sale.report"
    _description = "Sales Analysis Report"

    partner_id1 = fields.Many2one('res.partner', 'Customer1', readonly=True)

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        with_ = ("WITH %s" % with_clause) if with_clause else ""

        select_ = """
            
            s.partner_id1 as partner_id1,
            
        """

        for field in fields.values():
            select_ += field

        from_ = """
                
                      join res_partner partner on s.partner_id1 = partner.id1
                        
                %s
        """ % from_clause

        groupby_ = """
            s.partner_id1,
            %s
        """ % (groupby)

        return '%s (SELECT %s FROM %s GROUP BY %s)' % (with_, select_, from_, groupby_)
    
    def init(self):
        # self._table = sale_report
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""CREATE or REPLACE VIEW %s as (%s)""" % (self._table, self._query()))