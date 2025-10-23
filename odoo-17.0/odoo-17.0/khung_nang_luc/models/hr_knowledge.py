from odoo import models, fields

class HrKnowledge(models.Model):
    _name = 'hr.knowledge'
    _description = 'Danh mục kiến thức'

    name = fields.Char(string="Tên kiến thức", required=True)
    description = fields.Text(string="Mô tả")
    category = fields.Selection([
        ('ky_nang', 'Kỹ năng'),
        ('chuyen_mon', 'Chuyên môn'),
        ('khac', 'Khác')
    ], string="Loại kiến thức", default='ky_nang')
