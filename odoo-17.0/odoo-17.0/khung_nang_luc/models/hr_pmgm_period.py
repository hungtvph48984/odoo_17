from odoo import models, fields

class HrPmgmPeriod(models.Model):
    _name = 'hr.pmgm.period'
    _description = 'Chu kỳ đánh giá'

    name = fields.Char(string="Tên chu kỳ", required=True)
    date_start = fields.Date(string="Ngày bắt đầu")
    date_end = fields.Date(string="Ngày kết thúc")
    active = fields.Boolean(string="Kích hoạt", default=True)
