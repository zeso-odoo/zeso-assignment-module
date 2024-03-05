from odoo import api,fields,models

class StockPickingBatch(models.Model):
    _name="stock.picking.batch"
    _inherit = ["stock.picking.batch"]

    dock_id = fields.Many2one("stock.transport.dock")
    vehicle_id = fields.Many2one("fleet.vehicle.odometer")
    vehicle_category_id = fields.Many2one("fleet.vehicle.model.category",'Category')
    product_weight = fields.Float(string=' Product Weight')
    product_volume = fields.Float(string='Product Volume')
    max_weight = fields.Float(compute='_compute_total_weight',string='Weight')
    max_volume = fields.Float(compute='_compute_total_weight',string='Volume')

    @api.depends('max_volume','max_weight')
    def _compute_total_weight(self):
        for record in self:
            for product in record.move_line_ids:
                record.product_weight = product.product_id.weight * product.quantity
                record.product_volume = product.product_id.volume * product.quantity 
            record.max_weight = record.product_weight / record.vehicle_category_id.max_weight if record.vehicle_category_id.max_weight != 0 else 1
            record.max_volume = record.product_volume / record.vehicle_category_id.max_volume if record.vehicle_category_id.max_volume != 0 else 1
    

   
    
   

    
