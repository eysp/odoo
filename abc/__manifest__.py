{
    'name' : 'abc reports',
    'version': '1.2',
    'Summary': 'abcd Report Prints',
    'description': 'To print the new report',
    'license': 'LGPL-3',
    'depends': ['sale_management','website','account_accountant'],    
    'data': [
        #'data/data.xml',
        #'reports/report_tax_invoice.xml',
        #'reports/reports.xml',
        'views/testview.xml'
    ],
    'installable': True,
    'application':True,
    'auto_install':False
}