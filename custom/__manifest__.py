{
    'name' : 'Custom',
    'version': '1.0',
    'Summary': 'custom ',
    'description': 'for sir',
    'license': 'LGPL-3',
    'depends': [
        'sale_management','website','account_accountant'
    ],    
    'data': [
        'views/custom.xml',
        'reports/custom_report.py',
        'reports/custom_report_views.xml'
        
    ],
    'installable': True,
    'application':True,
    'auto_install':False
}