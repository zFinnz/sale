{
    'name': 'Quản lý bán hàng và Kho',
    'summary': 'Quản lý bán hàng và Kho',
    'description': 'Quản lý bán hàng và Kho',
    'category': 'Sale',
    'version': '14.0.1.0.0',
    'depends': ['web_backend', 'sale_management', 'stock', 'rowno_in_tree'],
    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/payment_views.xml',
        'views/sale_view.xml',
        'views/menu.xml',
    ],
    'application': True,
}