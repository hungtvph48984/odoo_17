from odoo import models,fields, api
from datetime import date
class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Real Estate Property"
    name = fields.Char("title", required=True)
    description = fields.Text("description")
    postcode = fields.Char("postcode")
    date_available = fields.date("date available", default = lambda self: date.today())
    expected_price = fields.Float("Expected Price", required=True)
    selling_price = fields.Float("Selling Price", readonly=True, copy=False)
    bedrooms = fields.Integer("Bedrooms", default=2)
    living_area = fields.Integer("Living Area (m²)")
    garden = fields.Boolean("Garden?")
    garden_area = fields.Integer("Garden Area (m²)")
    garden_orientation = fields.Selection(
        [('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
        string="Garden Orientation"
    )
    active = fields.Boolean("Active", default=True)
    property_type_id = fields.Many2one("estate.type", string="Property Type")
    tag_ids = fields.Many2many("estate.tag", string="Tags")
    salesperson_id = fields.Many2one("res.users", string="Salesperson", default=lambda self: self.env.user)

    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            self.garden_area = 0
            self.garden_orientation = False