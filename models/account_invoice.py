from openerp import models, api, fields

class AccountInvoice(models.Model):
    _inherit = 'account.invoice'

    @api.onchange('journal_id')
    def _onchange_journal_id(self):
        super(AccountInvoice, self)._onchange_journal_id()
        bob_currency = self.env['res.currency'].search([('name', '=', 'BOB')], limit=1)
        if bob_currency:
            self.currency_id = bob_currency

class AccountInvoiceLine(models.Model):
    _inherit = 'account.invoice.line'

    currency_id = fields.Many2one(
        'res.currency', string='Currency',
        default=lambda self: self.env['res.currency'].search([('name', '=', 'BOB')], limit=1)
    )
