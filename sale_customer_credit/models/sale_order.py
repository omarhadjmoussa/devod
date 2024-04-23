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
#############################################################################
from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    customer_credit = fields.Float(string='Customer Credit', compute='_compute_customer_credit')

    @api.depends('partner_id')
    def _compute_customer_credit(self):
        for order in self:
            if order.partner_id:
                order.customer_credit = order.partner_id.credit
            else:
                order.customer_credit = 0.0