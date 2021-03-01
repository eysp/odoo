{
    'name' : 'Task@mar1',
    'version': '1.0',
    'Summary': 'Task given on mar 1 2021',
    'description': 'To add new button for crating sale order from mar 1 2021',
    'license': 'LGPL-3',
    'depends': [
        'sale_management',
        'purchase',
        'project',
        'account_accountant',
        'product'
    ],    
    'data': [
        views/task_view.xml
    ],
    'installable': True,
    'application':True,
    
}