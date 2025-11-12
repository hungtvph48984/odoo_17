from odoo import models, fields

class EstateTag(models.Model):
    _name = "estate.tag"
    _description = "Estate Tag"

    name = fields.Char("Tag Name", required=True)
    property_ids = fields.Many2many("estate.property", "estate_property_tag_rel", "tag_id", "property_id", string="Properties")
