from odoo import api,fields,models

class StockTransportDoc(models.Model):
    _name="stock.transport.dock"
    _description="stock transport dock"

    name=fields.Char(required=True)
