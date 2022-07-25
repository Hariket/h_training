from odoo import api, fields, models


class StockLocationKsc(models.Model):
    _name = 'stock.location.ksc'
    _description = 'Stock Localization'

    name = fields.Char(string='Name', required=True)
    parent_id = fields.Many2one('stock.location.ksc')
    location_type = fields.Selection([('vendor', 'Vendor'), ('customer', 'Customer'),
                                      ('internal', 'Internal'), ('inventory', 'Inventory'),
                                      ('loss', 'Loss'), ('production', 'Production'),
                                      ('transit', 'Transit'), ('view', 'View')],
                                     string='Location Type')
    is_scrap_location = fields.Boolean('Is Scrap Location')
