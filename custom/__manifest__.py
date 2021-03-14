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
        
         'report/custom_report_views.xml',
        # 'report/custom_report_templates.xml',
         'report/custom_report.xml'
        
    ],
    'installable': True,
    'application':True,
    'auto_install':False
}