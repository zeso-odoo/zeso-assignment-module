from odoo import fields,api,models

class ResConfigSettings(models.TransientModel):
    
    _inherit=['res.config.settings']

    module_stock_transport = fields.Boolean("Dispatch Management System")
    