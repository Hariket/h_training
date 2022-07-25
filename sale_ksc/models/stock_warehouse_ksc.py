from odoo import api, fields, models


class StockWarehouseKsc(models.Model):
    _name = 'stock.warehouse.ksc'
    _description = 'Stock Warehouse'

    name = fields.Char(string='Name', required=True)
    short_code = fields.Char(string='Short Code', required=True)
    address = fields.Many2one('res.partner.ksc', string='Address')
    stock_location_id = fields.Many2one('stock.location.ksc')
    view_location_id = fields.Many2one('stock.location.ksc')

