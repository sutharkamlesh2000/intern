from odoo import models, fields


class Products(models.Model):
    _inherit = "product.template"

    quantity = fields.Integer('Quantity')