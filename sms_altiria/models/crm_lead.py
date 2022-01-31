from odoo import models, fields


class Company(models.Model):
    _inherit = 'crm.lead'

    phone_new = fields.Char(string='phone number')