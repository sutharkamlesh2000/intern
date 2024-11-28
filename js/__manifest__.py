
{
    'name': 'JS Practice',
    'version': '17.0.1.0',
    'license': 'LGPL-3',
    'category': 'Education',
    "sequence": 3,
    'depends': ['website'],
    'data': [
        'views/template_products_view.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'js/static/src/js/products_list.js',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
}
