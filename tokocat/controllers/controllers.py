
from odoo import http,  models, fields
from odoo.http import request
import json


class Tokocat(http.Controller):
    @http.route('/tokocat/getcat', auth='public', method=['GET'])
    def getcat(self, **kw):
        cat = request.env['tokocat.cat'].search([])
        isi = []
        for bb in cat:
            isi.append({
                'nama_cat': bb.name,
                'harga_jual': bb.harga_jual,
                'stock': bb.stock
            })
        return json.dumps(isi)

    @http.route('/tokocat/getsupplier', auth='public', method=['GET'])
    def getSupplier(self, **kw):
        supplier = request.env['tokocat.supplier'].search([])
        sup = []
        for s in supplier:
            sup.append({
                'nama_perusahaan': s.name,
                'alamat': s.alamat,
                'no_telepon': s.no_telp,
                'cat': s.cat_id[0].name
            })
        return json.dumps(sup)
