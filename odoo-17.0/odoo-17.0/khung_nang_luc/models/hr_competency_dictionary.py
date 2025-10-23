from odoo import models, fields

class HrCompetencyDictionary(models.Model):
    _name = 'hr.competency.dictionary'
    _description = 'Từ điển năng lực'

    name = fields.Char(string="Tên năng lực", required=True)
    description = fields.Text(string="Mô tả năng lực")
    level_id = fields.Many2one('hr.competency.level', string="Cấp độ liên quan")
