# -*- coding: utf-8 -*-
from odoo import fields, models, api

class Employee(models.Model):
    _inherit = "hr.employee"

    info = fields.Char(string="Employee Info", compute="_compute_info", store=True)

    @api.depends('work_email', 'work_phone')
    def _compute_info(self):
        for rec in self:
            rec.info = " - ".join(filter(None, [rec.work_email, rec.work_phone])) or ""
