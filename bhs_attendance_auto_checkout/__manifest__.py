# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'BHSoft attendance auto checkout',
    'version': '1.0',
    'category': 'Human Resources',
    'sequence': 335,
    'description': """
        Automaticaly check out by time admin configure
    """,
    'website': 'https://www.odoo.com/app/employees',
    'depends': ['hr_attendance'],
    'data': [
        'views/attendance_auto_checkout.xml',
        'data/attendance_data.xml',
    ],
    'license': 'LGPL-3',
    'images': ['static/description/banner.gif'],
    # Author
    'author': 'Bac Ha Software',
    'website': 'https://bachasoftware.com',
    'maintainer': 'Bac Ha Software',

    'installable': True,
    'application': True,
    'auto_install': False,
}
