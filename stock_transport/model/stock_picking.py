from odoo import fields,models,api

class StockLineMove(models.Model):
    _name = 'stock.picking'
    _inherit = ['stock.picking']

    total_volume = fields.Float('Volume',compute ="_compute_total_volume")

    @api.depends('total_volume')
    def _compute_total_volume(self):
        for record in self:
            record.total_volume = record.product_id.volume
            