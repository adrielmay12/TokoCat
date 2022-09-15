from odoo import api, fields, models


class Supplier(models.Model):
    _name = 'tokocat.supplier'
    _description = 'New Description'

    name = fields.Char(string='Nama Perusahaan')
    alamat = fields.Char(string='Alamat')
    no_telp = fields.Char(string='No. Telpon')
    cat_id = fields.Many2many(comodel_name='tokocat.cat', string='Cat')
    kebutuhan = fields.Many2many(
        comodel_name='tokocat.kebutuhanlain', string='Kebutuhan Lain')
