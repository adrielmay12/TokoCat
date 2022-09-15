from odoo import api, fields, models


class Konsumen(models.Model):
    _inherit = 'res.partner'
    _description = 'konsumen'

    is_konsumen = fields.Boolean(string='Is Konsumen')
    poin = fields.Integer(string='Poin')
    level = fields.Char(string='Level')
