{
    'name': 'Stock Transport',
    'version': '1.0',
    'summary': 'stock transport application',
    'depends':[
        'base',
        'fleet',
        'stock_picking_batch',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/stock_picking_view.xml',
        'views/tms_stock_transport_view.xml',
        'views/tms_stock_picking_batch_view.xml',  
    ],
    'installable': True,
    'application':True,
    'license': 'LGPL-3',
}
