# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models


class SendSMS(models.TransientModel):
    _inherit = 'sms.composer'
    _description = 'Send SMS Wizard'

    def action_send_sms_mass_now(self):
        sms_api = self.env['sms.api']
        self.composition_mode = 'mass'
        active_ids = self.env.context.get('active_ids', False) or self.env.context.get('default_res_id', False) or self.env.context.get('default_res_ids', False)
        model = self.env[self.res_model]
        records = model.browse(active_ids)
        numbers = []
        msg = self.body
        for record in records.filtered(lambda r: r.mobile):
            numbers.append(record.mobile)
        sms_api.with_context(self.env.context)._send_sms(numbers, msg)

    def action_send_sms(self):
        self.action_send_sms_mass_now()