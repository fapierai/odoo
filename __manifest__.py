# -*- coding: utf-8 -*-
{
    'name': "My Module",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose
    """,
    'description': """
        Long description of module's purpose
    """,
    'author': "Fapier",
    'website': "https://www.fapier.com",
    'category': 'Uncategorized',
    'version': '18.0.1.0.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
    # Odoo 18 constraints
    'odoo_version': '18.0',
    'external_dependencies': {
        'python': [],
        'bin': []
    },
    'maintainer': 'Fapier',
    'repository': 'https://github.com/fapierai/odoo.git',
}
