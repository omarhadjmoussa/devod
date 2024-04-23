# -*- coding: utf-8 -*-
#############################################################################
#
#    Omar hm. Dev.
#
#    Copyright (C) 2024-TODAY Omar hm. Dev(omarhadjmoussa@gmail.com).
#    Author: omar hadj moussa(omarhadjmoussa@gmail.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#
#############################################################################
{
    'name': 'Customer credit in sale order',
    'version': '17.0.1.0.0',
    'category': 'Sales Management',
    'summary': "Customer credit in Sale",
    'description': "This module is designed to cosult the credit customer in sales. "
                   "This module will enhance the functionality of Odoo's sales module,"
                   "allowing users to easily manage and consult the credit customer in sales orders.",
    'author': 'Omar HADJ MOUSSA',
    'company': 'Omar hm. Dev',
    'maintainer': 'Omar hm. Dev',
    'website': "omarhadjmoussa@gmail.com",
    'depends': ['sale_management'],
    'data': [
        'views/sale_order_views.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
