from odoo import api, fields, models


class BarangDatang(models.TransientModel):
    _name = 'tokocat.barangdatang'

    barang_id = fields.Many2one(
        comodel_name='tokocat.cat',
        string='Nama Barang',
        required=True)

    jumlah = fields.Integer(
        string='Jumlah',
        required=False)

    def button_barang_datang(self):
        for rec in self:
            self.env['tokocat.cat'].search([('id', '=', rec.barang_id.id)]).write(
                {'stock': rec.barang_id.stock + rec.jumlah})
