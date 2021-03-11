{
    'name' : 'Test model',
    'version': '1.2',
    'Summary': 'Trial new custom model',
    'description': 'first module',
    'license': 'LGPL-3',
    'depends': [
        'sale_management','website','account_accountant'
    ],    
    'data': [
        #'data/data.xml',
        #'reports/report_tax_invoice.xml',
        #'reports/reports.xml',
        #'views/app_report_testview.xml'
    ],
    'installable': True,
    'application':True,
    'auto_install':False
}