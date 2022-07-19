from odoo import api, models
from collections import defaultdict


class ProductPrcking(models.AbstractModel):
    _name = 'report.my_sale_extended.report_groupby_product_picking'

    @api.model
    def _get_report_values(self, docids, data=None):
        selected_pickings_recs = self.env['stock.picking'].browse(docids)
        products = selected_pickings_recs.mapped('move_line_ids.product_id')
        warehouses = defaultdict(list)

        if products:
            for product in products:
                matching_pickings = selected_pickings_recs.filtered(
                    lambda p: product in p.mapped('move_line_ids.product_id'))
                picking_qty_list = [{
                    picking.name:
                        sum(picking.move_line_ids.filtered(lambda x: product in x.mapped('product_id')).mapped(
                            'product_uom_qty'))
                } for picking in matching_pickings]
                warehouses.update({product: picking_qty_list})
        return {
            "data": data,
            "docs": self.env['stock.picking'].browse(docids[0]),
            "line": warehouses
        }
