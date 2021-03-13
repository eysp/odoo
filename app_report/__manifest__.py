{
    'name' : 'Tax Reports',
    'version': '1.3',
    'Summary': 'Tax Report Prints',
    'description': 'To print the new report',
    'license': 'LGPL-3',
    'depends': [
        'sale_management','website','account_accountant','sales_team'
    ],    
    'data': [
        'reports/report_tax_invoice.xml',
        'reports/reports.xml',
        'views/app_report_view.xml'
    ],
    'installable': True,
    'application':True,
    'auto_install':False
}