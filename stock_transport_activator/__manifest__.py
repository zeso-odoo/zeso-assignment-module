{
    'name':'stock Transport Activator',
    'version': '1.0',
    'summary': 'Dispatch management system',
    'depends':[
        'base',
        'fleet',
        'stock_picking_batch',
    ],
    'data': [
        'views/res_config_settings_view.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}