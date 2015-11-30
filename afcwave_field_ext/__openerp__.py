# -*- coding: utf-8 -*-
{
    "name": "AFC WAVE Extends Module",
    "version": "1.0",
    'author': 'Falinwa Hans',
    "description": """
    Module to add additional field for AFC WAVE
    """,
    "depends" : [
        'base', 'report', 'stock', 'sale', 'portal_sale', 'fal_portal_sale_ext'
        ],
    'init_xml': [],
    'update_xml': [
        #'security/ir.model.access.csv',
        'sale_view.xml',
    ],
    'css': [],
    'js' : [],
    'installable': True,
    'active': False,
    'application' : False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: