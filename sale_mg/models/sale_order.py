# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from random import randint

from odoo import fields, models, api

class ProductTemplate(models.Model):
    _inherit = "product.template"

    @api.model
    def default_get(self, fields):
        res = super(ProductTemplate, self).default_get(fields)
        res['type'] = 'product'
        return res


class SaleOrder(models.Model):
    _inherit = "sale.order"

    cus_phone = fields.Char(string='Số điện thoại')
    cus_address = fields.Char(string='Địa chỉ')
    cus_info = fields.Char(string='Thông tin khách')
    product_name = fields.Char(string='Tên sản phẩm', compute='_compute_product_name', store=True)
    sale_qty = fields.Integer(string='Số lượng', compute='_compute_sale_qty', store=True)
    sale_weight = fields.Float(string='Trọng lượng', default=0.3)

    shipping_amount = fields.Monetary(string='Phí COD', default=30000)
    total_shipping_amount = fields.Monetary(related='amount_total', string='Tiền COD')

    @api.depends("order_line.product_id")
    def _compute_product_name(self):
        for rec in self:
            rec.product_name = ', '.join([line.product_id.display_name for line in rec.order_line if line.product_id])

    @api.depends("order_line.product_uom_qty")
    def _compute_sale_qty(self):
        for rec in self:
            rec.sale_qty = sum([line.product_uom_qty for line in rec.order_line])

    @api.depends('order_line.price_total')
    def _amount_all(self):
        """
        Compute the total amounts of the SO.
        """
        for order in self:
            amount_untaxed = amount_tax = 0.0
            for line in order.order_line:
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax
            order.update({
                'amount_untaxed': amount_untaxed,
                'amount_tax': amount_tax,
                'amount_total': amount_untaxed + amount_tax + order.shipping_amount,
            })


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    date_order = fields.Datetime(related='order_id.date_order', string='Ngày đặt hàng', store=True)

    qty_available = fields.Float(related='product_id.qty_available', string='SL tồn kho')
    virtual_available = fields.Float(related='product_id.virtual_available', string='SL khả dụng')

    is_need_purchase = fields.Boolean(string='Thiếu hàng', compute='_compute_is_need_purchase', store=True)

    @api.depends("product_uom_qty", "virtual_available")
    def _compute_is_need_purchase(self):
        for rec in self:
            rec.is_need_purchase = rec.product_uom_qty > rec.virtual_available

