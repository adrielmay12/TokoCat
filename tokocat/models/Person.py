from odoo import api, fields, models


class Person(models.Model):
    _name = 'tokocat.person'
    _description = 'New Description'

    name = fields.Char(string='Nama')
    alamat = fields.Char(string='Alamat')
    tgl_lahir = fields.Datetime('Tanggal Lahir')


class Kasir(models.Model):
    _name = 'tokocat.kasir'
    _description = 'New Description'
    _inherit = 'tokocat.person'
    id_kasir = fields.Char(string='ID Kasir')


# class CleaningService(models.Model):
#     _name = 'elmart.cleaningservice'
#     _description = 'New Description'
#     _inherit = 'elmart.person'
#     id_cln = fields.Char(string='ID Cleaning Service')
