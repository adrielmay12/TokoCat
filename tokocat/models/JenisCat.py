from odoo import api, fields, models


class JenisCat(models.Model):
    _name = 'tokocat.jeniscat'
    _description = 'New Description'

    name = fields.Selection([
        ('catbesi', 'Cat Besi'),
        ('catkayu', 'Cat Kayu'),
        ('cattembok', 'Cat Tembok'),
        ('catgenteng', 'Cat Genteng'),
        ('catduco', 'Cat Duco')
    ], string='Nama kelompok')

    kode_cat = fields.Char(string='Kode Cat')

    @api.onchange('name')
    def _compute_kode_cat(self):
        if (self.name == 'catbesi'):
            self.kode_cat = 'cat01'
        elif (self.name == 'catkayu'):
            self.kode_cat = 'cat02'
        elif (self.name == 'cattembok'):
            self.kode_cat = 'cat03'
        elif (self.name == 'catgenteng'):
            self.kode_cat = 'cat04'
        elif (self.name == 'catduco'):
            self.kode_cat = 'cat05'

    kode_rak = fields.Char(string='Kode Rak')
    barang_ids = fields.One2many(comodel_name='tokocat.cat',
                                 inverse_name='kelompokbarang_id',
                                 string='Daftar Barang')

    jml_item = fields.Char(compute='_compute_jml_item', string='Jumlah Item')

    @api.depends('barang_ids')
    def _compute_jml_item(self):
        for rec in self:
            a = self.env['tokocat.cat'].search(
                [('kelompokbarang_id', '=', rec.id)]).mapped('name')
            b = len(a)
            rec.jml_item = b
            rec.daftar = a

    daftar = fields.Char(string='Daftar Isi')
