# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Web Backend',
    'category': 'Hidden',
    'version': '1.0',
    'description':
        """
Odoo Backend Web Client.
===========================

This module modifies the web addon to provide Enterprise design and responsiveness.
        """,
    'depends': ['web'],
    'auto_install': False,
    'data': [
        'views/webclient_templates.xml',
        'views/st_webclient_templates.xml',
        
    ],
    'qweb': [
        "static/src/xml/*.xml",
    ],
    'license': 'OEEL-1',
}
