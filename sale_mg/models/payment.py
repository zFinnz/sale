from num2words import num2words
from odoo import fields, models, api, _, exceptions
from odoo.exceptions import ValidationError, UserError


class PaymentBook(models.Model):
	_name = 'payment.book'

	name = fields.Char(string='Tên')

	payments = fields.One2many('sale.payment', 'book_id', string=u'Chi tiết', readonly=True)
	total_payment = fields.Float(u'Tổng chi', compute='_compute_total', store=True, digits=(12, 0))
	total_recieve = fields.Float(u'Tổng thu', compute='_compute_total', store=True, digits=(12, 0))
	total_residual = fields.Float(u'Số dư', compute='_compute_total', store=True, digits=(12, 0))

	@api.depends('payments', 'payments.total_payment', 'payments.total_recieve')
	def _compute_total(self):
		for book in self:
			book.total_payment = sum([line.total_payment for line in book.payments])
			book.total_recieve = sum([line.total_recieve for line in book.payments])
			book.total_residual = book.total_recieve - book.total_payment


class SalePayment(models.Model):
	_name = 'sale.payment'

	def _get_book_id_default(self):
		book_ids = self.env['payment.book'].search([])
		if len(book_ids) == 1:
			return book_ids.id

	book_id = fields.Many2one('payment.book', string=u'Sổ', ondelete='cascade', required=True, default=_get_book_id_default)
	user_id = fields.Many2one('res.users', u'Người tạo', readonly=True, default=lambda self: self.env.user)
	payment_date = fields.Date(u'Ngày thực hiện')
	note = fields.Char(u'Diễn giải', required=True)
	total_payment = fields.Float(u'Tổng chi', digits=(12, 0))
	total_recieve = fields.Float(u'Tổng thu', digits=(12, 0))
