{
    'name': 'Khung Năng Lực',
    'version': '1.0',
    'summary': 'Quản lý khung năng lực nhân sự',
    'category': 'Human Resources',
    'author': 'UIT Student',
    'website': 'https://uit.edu.vn',
    'depends': ['base', 'hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_knowledge_views.xml',
        'views/hr_competency_level_views.xml',
        'views/hr_competency_dictionary_views.xml',
        'views/hr_pmgm_period_views.xml',
    ],
    'installable': True,
    'application': True,
}
