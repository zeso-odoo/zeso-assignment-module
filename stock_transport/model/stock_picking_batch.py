from odoo import api,fields,models
from odoo.exceptions import UserError

class StockPickingBatch(models.Model):
    _name="stock.picking.batch"
    _inherit = ["stock.picking.batch"]

    dock_id = fields.Many2one("stock.transport.dock")
    vehicle_id = fields.Many2one("fleet.vehicle.odometer")
    vehicle_category_id = fields.Many2one("fleet.vehicle.model.category",'Category')
    product_weight = fields.Float(string=' Product Weight')
    product_volume = fields.Float(string='Product Volume')
    max_weight = fields.Float(compute='_compute_total_weight',string='Weight')
    max_volume = fields.Float(compute='_compute_total_volume',string='Volume')
    transfers = fields.Integer(string="Transfers")
    lines = fields.Integer(string='Lines')

    @api.depends('picking_ids.move_line_ids.product_id.volume','picking_ids.move_line_ids')
    def _compute_total_volume(self):
        total = self.picking_ids.move_line_ids
        total_volume=0
        for record in total:
            total_volume = total_volume + record.product_id.volume * record.quantity
        self.max_volume = (total_volume/(self.vehicle_category_id.max_volume if self.vehicle_category_id.max_volume  != 0 else 1)) * 100
        
    
    @api.depends('picking_ids.move_line_ids.product_id.volume','picking_ids.move_line_ids')
    def _compute_total_weight(self):
        total = self.picking_ids.move_line_ids
        total_weight=0
        for record in total:
            total_weight = total_weight + record.product_id.weight * record.quantity
        self.max_weight = (total_weight/(self.vehicle_category_id.max_weight if self.vehicle_category_id.max_weight != 0 else 1 )) * 100     
        