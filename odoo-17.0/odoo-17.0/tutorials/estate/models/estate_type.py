from odoo import models, fields

class EstateType(models.Model):
    _name = "estate.type"
    _description = "Estate Type"

    name = fields.Char("Type Name", required=True)
    property_ids = fields.One2many("estate.property", "property_type_id", string="Properties")
