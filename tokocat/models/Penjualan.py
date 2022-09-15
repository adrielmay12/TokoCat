from odoo import api, fields, models
from odoo . exceptions import UserError, ValidationError


class Penjualan(models.Model):
    _name = 'tokocat.penjualan'
    _description = 'New Description'

    name = fields.Char(string='No. Nota')
    nama_pembeli = fields.Char(string='Nama Pembeli')
    tgl_penjualan = fields.Datetime(
        string='Tgl. Transaksi', default=fields.Datetime.now())
    total_bayar = fields.Integer(
        compute='_compute_totalbayar', string='Total Pembayaran')
    detailpenjualan_ids = fields.One2many(
        comodel_name='tokocat.detailpenjualan',
        inverse_name='penjualan_id',
        string='Detail Penjualan')

    state = fields.Selection(
        string='Status',
        selection=[('draft', 'Draft'),
                   ('confirm', 'Confirm'),
                   ('done', 'Done'),
                   ('cancelled', 'Cancelled'),
                   ],
        required=True, readonly=True, default="draft")

    def action_confirm(self):
        self.write({'state': 'confirm'})

    def action_done(self):
        self.write({'state': 'done'})

    def action_cancel(self):
        self.write({'state': 'cancelled'})

    def action_draft(self):
        self.write({'state': 'draft'})

    @api.depends('detailpenjualan_ids')
    def _compute_totalbayar(self):
        for rec in self:
            a = sum(self.env['tokocat.detailpenjualan'].search(
                [('penjualan_id', '=', rec.id)]).mapped('subtotal'))
            rec.total_bayar = a

    # @api.ondelete(at_uninstall=False)
    # def __ondelete_penjualan(self):
    #     if self.detailpenjualan_ids:
    #         a = []
    #         for rec in self:
    #             a = self.env['tokocat.detailpenjualan'].search(
    #                 [('penjualan_id', '=', rec.id)])
    #             print(a)
    #         for ob in a:
    #             print(str(ob.barang_id.name) + '' + str(ob.qty))
    #             ob.barang_id.stock += ob.qty

    def unlink(self):
        if self.filtered(lambda line: line.state != 'draft'):
            raise ValidationError(
                "Jika status bukan draft maka tidak dapat dihapus")
        else:
            if self.detailpenjualan_ids:
                a = []
                for rec in self:
                    a = self.env['tokocat.detailpenjualan'].search(
                        [('penjualan_id', '=', rec.id)])
                    print(a)
                for ob in a:
                    print(str(ob.barang_id.name) + '' +
                          str(ob.qty)+' '+str(ob.barang_id.stock))
                    ob.barang_id.stock += ob.qty
        record = super(Penjualan, self).unlink()

    def write(self, vals):
        for rec in self:
            a = self.env['tokocat.detailpenjualan'].search(
                [('penjualan_id', '=', rec.id)])
            print(a)
            for data in a:
                print(str(data.barang_id.name)+' '+str(data.qty))
                data.barang_id.stock += data.qty
        record = super(Penjualan, self).write(vals)
        for rec in self:
            b = self.env['tokocat.detailpenjualan'].search(
                [('penjualan_id', '=', rec.id)])
            print(a)
            print(b)
            for databaru in b:
                if databaru in a:
                    print(str(databaru.barang_id.name)+' ' +
                          str(databaru.qty)+' '+str(databaru.barang_id.stock))
                    databaru.barang_id.stock -= databaru.qty
                else:
                    pass
        return record

    _sql_constraints = [
        ('no_nota_unik', 'unique (name)', 'Nomor Nota tidak boleh sama!!!')
    ]


class DetailPenjualan(models.Model):
    _name = 'tokocat.detailpenjualan'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    penjualan_id = fields.Many2one(
        comodel_name='tokocat.penjualan', string='Detail Penjualan')
    barang_id = fields.Many2one(
        comodel_name='tokocat.cat', string='List Barang')
    # warna_ids = fields.Many2one(
    #     comodel_name='tokocat.cat', inverse_name='kelompok_warna', string='List Warna Tersedia')
    harga_satuan = fields.Integer(string='Harga Satuan')
    qty = fields.Integer(string='Quantity')
    subtotal = fields.Integer(compute='_compute_subtotal', string='Subtotal')

    @api.depends('harga_satuan', 'qty')
    def _compute_subtotal(self):
        for rec in self:
            rec.subtotal = rec.qty * rec.harga_satuan

    @api.onchange('barang_id')
    def _onchange_barang_id(self):
        if (self.barang_id.harga_jual):
            self.harga_satuan = self.barang_id.harga_jual

    @api.model
    def create(self, vals):
        record = super(DetailPenjualan, self).create(vals)
        if record.qty:
            self.env['tokocat.cat'].search([('id', '=', record.barang_id.id)]).write({
                'stock': record.barang_id.stock - record.qty})
        return record

    @api.constrains('qty')
    def check_quantity(self):
        for rec in self:
            if rec.qty < 1:
                raise ValidationError(
                    "Mau belanja {} berapa banyak sih ??".format(rec.barang_id.name))
            elif (rec.barang_id.stock < rec.qty):
                raise ValidationError("Stock {} tidak mencukupi, hanya tersedia {} ".format(
                    rec.barang_id.name, rec.barang_id.stock))
