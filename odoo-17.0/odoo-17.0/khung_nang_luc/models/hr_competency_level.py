from odoo import models, fields

class HrCompetencyLevel(models.Model):
    _name = 'hr.competency.level'
    _description = 'Cấp độ năng lực'

    name = fields.Char(string="Tên cấp độ", required=True)
    score = fields.Integer(string="Điểm số")
    note = fields.Text(string="Ghi chú")
