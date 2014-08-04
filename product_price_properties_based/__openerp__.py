# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014 Agile Business Group sagl
#    (<http://www.agilebg.com>)
#    @author Lorenzo Battistini <lorenzo.battistini@agilebg.com>
#    @author Alex Comba <alex.comba@agilebg.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "Product price properties based",
    'version': '0.1',
    'category': '',
    'description': """

Contributors
------------

 - Lorenzo Battistini <lorenzo.battistini@agilebg.com>
 - Alex Comba <alex.comba@agilebg.com>

    """,
    'author': 'Agile Business Group',
    'website': 'http://www.agilebg.com',
    'license': 'AGPL-3',
    "depends": [
        'sale_properties_easy',
    ],
    "data": [
        'sale_view.xml',
    ],
    "demo": [
        'sale_demo.xml',
        ],
    "test": [
        'test/sale_order.yml',
        ],
    "active": False,
    "installable": True
}