# -*- coding: utf-8 -*-
{
    'name': "Menu official",

    'summary': """
        Menu modulos""",

    'description': """
        Varios modulos en un solo menu!
    """,

    'author': "erick",
    'website': "http://www.soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','hr','hr_holidays','survey',
                'hr_skill','employee_orientation',
                'knowledge','org_chart_dept','mgmtsystem',
                'mgmtsystem_action','mgmtsystem_audit',
                'mgmtsystem_review','mgmtsystem_hazard',
                'mgmtsystem_nonconformity','company_profile'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
#       'views/views.xml',
#       'views/templates.xml',
#       'views/hr.xml',
        'views/views.xml',
        'views/advise.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
     #   'demo/demo.xml',
    ],
    'installable': True,
}
