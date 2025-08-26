from odoo import models, fields, api


class PracConnectorBase(models.Model):
    _inherit = 'odoo.connector.base'


    integration = fields.Selection(
        selection_add=[
            ("rracks_fetch_cnal", "Fetch data : CNAL"),
            ("rracks_fetch_boc", "Fetch data : BOC"),
        ],
    )


    # Override the run method to handle custom integrations


    def run(self, *args, **kwargs):
        self.ensure_one()
        res = super(PracConnectorBase, self).run(*args, **kwargs)
        integration = self.integration
        match integration:
            case "rracks_fetch_cnal":
                self.rracks_fetch_cnal()
                return res
            case "rracks_fetch_boc":
                self.rracks_fetch_boc()
                return res
        return res