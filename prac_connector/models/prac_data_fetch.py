from odoo import models, fields, api



class PracDataFetch(models.Model):
    _name = 'prac.data.fetch'
    _description = 'Prac Data Fetch'
    _rec_name = 'name'

    name = fields.Char(
        string='Name',
        compute='_compute_name',
        store=True,
    )
    type = fields.Selection(
        string='Type',
        selection=[
            ('cnal', 'CNAL'),
            ('boc', 'BOC'),
        ],
        required=True,
    )
    date = fields.Date(
        string='Date',
        default=fields.Date.context_today,
    )
    full_data = fields.Text(
        string='Full Data Fetched',
    )
    data = fields.Char(
        string='Data',
    )

    @api.depends('type', 'date')
    def _compute_name(self):
        for record in self:
            record.name = f"{record.type}-{record.date}" if record.date else record.type