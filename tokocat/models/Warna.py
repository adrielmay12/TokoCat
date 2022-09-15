from odoo import api, fields, models


class KelompokWarna(models.Model):
    _name = 'tokocat.kelompokwarna'
    _description = 'New Description'

    name = fields.Selection([
        ('merah', 'Merah'),
        ('kuning', 'Kuning'),
        ('putih', 'Putih'),
        ('abuabu', 'Abu-abu'),
        ('cream', 'Cream'),
        ('coklat', 'Coklat'),
        ('hitam', 'Hitam'),
        ('biru', 'Biru'),
        ('silver', 'Silver'),
        ('hijau', 'Hijau')
    ], string='Warna Cat')

    kode_warnacat = fields.Char(string='Kode Warna Cat')

    @api.onchange('name')
    def _compute_kode_warnacat(self):
        if (self.name == 'merah'):
            self.kode_warnacat = 'm1'
        elif (self.name == 'kuning'):
            self.kode_warnacat = 'k1'
        elif (self.name == 'putih'):
            self.kode_warnacat = 'p1'
        elif (self.name == 'abuabu'):
            self.kode_warnacat = 'a1'
        elif (self.name == 'cream'):
            self.kode_warnacat = 'c1'
        elif (self.name == 'coklat'):
            self.kode_warnacat = 'c2'
        elif (self.name == 'hitam'):
            self.kode_warnacat = 'h1'
        elif (self.name == 'biru'):
            self.kode_warnacat = 'b1'
        elif (self.name == 'silver'):
            self.kode_warnacat = 's1'
        elif (self.name == 'hijau'):
            self.kode_warnacat = 'h2'

    kode_rak = fields.Char(string='Kode Rak')
    warna_id = fields.Many2many(
        comodel_name='tokocat.cat', string='Daftar Isi')

    # barang_ids = fields.One2many(comodel_name='tokocat.cat',
    #                              inverse_name='kelompokbarang_id',
    #                              string='Daftar Barang')

    # daftar = fields.Char(string='Daftar Isi')
