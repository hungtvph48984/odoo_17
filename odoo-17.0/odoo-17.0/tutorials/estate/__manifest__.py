{
    'name': "Real Estate",
    'version': '1.0',
    'depends': ['base'],
    'author': "UIT Student",
    'category': 'Real Estate',
    'summary': "Manage properties, buyers, and offers",
    'description': "A simple real estate module for property management.",
    'data': [
        'security/ir.model.access.csv',
        'views/menu_items.xml',
        'views/estate_property_views.xml',
        'views/estate_type_views.xml',
        'views/estate_tag_views.xml',
    ],
    'application': True,
}
