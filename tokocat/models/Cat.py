from odoo import api, fields, models


class Cat(models.Model):
    _name = 'tokocat.cat'
    _description = 'New Description'

    name = fields.Char(string='Nama Cat')
    harga_beli = fields.Integer(string='Harga Modal', required=True)
    harga_jual = fields.Integer(string='Harga Jual', required=True)
    kelompokbarang_id = fields.Many2one(
        comodel_name='tokocat.jeniscat', string='Jenis Cat', ondelete='cascade')

    supplier_id = fields.Many2many(
        comodel_name='tokocat.supplier', string='Supplier')
    stock = fields.Integer(string='Stock')

    kelompok_warna = fields.Many2many(comodel_name='tokocat.kelompokwarna',
                                      string='Kelompok Warna Cat')
