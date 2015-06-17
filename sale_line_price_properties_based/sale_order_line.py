# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2014-15 Agile Business Group sagl
#    (<http://www.agilebg.com>)
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

from openerp import models, api
from openerp.tools.translate import _
from openerp.exceptions import except_orm


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange(
        'property_ids', 'product_id', 'product_uom_qty', 'product_uom'
    )
    def price_property_ids_changed(self):
        prop_dict = {}
        prop_ctx = self.env.context.copy()
        if 'lang' in prop_ctx:
            del prop_ctx['lang']
        if self.product_id:
            for prop in self.env['mrp.property'].with_context(prop_ctx).browse(
                [p.id for p in self.property_ids]
            ):
                if prop.group_id.name in prop_dict:
                    raise except_orm(
                        _('Error'),
                        _('Property of group %s already present')
                        % prop.group_id.name)
                prop_dict[prop.group_id.name] = prop.value
            self.price_unit = self.pool.get('product.pricelist').price_get(
                self._cr, self._uid, [self.order_id.pricelist_id.id],
                self.product_id.id, self.product_uom_qty or 1.0,
                self.order_id.partner_id.id, {
                    'uom': self.product_uom.id,
                    'date': self.order_id.date_order,
                    'properties': prop_dict,
                })[self.order_id.pricelist_id.id]