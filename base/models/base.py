from odoo import models, fields, api
"""
Base model for Odoo Connector Addons
This module provides a base model for Odoo connector addons, allowing for
the creation of connector configurations and integration methods.

"""


class OdooConnectorBase(models.Model):
    _name = 'odoo.connector.base'
    _description = 'Odoo Connector Base Configuration'
    _rec_name = 'name'


    name = fields.Char(
        string='Name',
        required=True,
        help='Name of the connector configuration',
    )
    active = fields.Boolean(
        string='Active',
        default=True,
        help='Whether the connector configuration is active',
    )
    base_url = fields.Char(
        string='Base URL',
        help='Base URL for the connector',
    )
    authentication_method = fields.Selection(
        selection=[
            ('basic', 'Basic Auth'),
            ('oauth2', 'OAuth2'),
            ('api_key', 'API Key'),
        ],
        string='Authentication Method',
        help='Method of authentication for the connector',
    )

    authentication_details = fields.Text(
        string='Authentication Details',
        help='Details required for the selected authentication method',
    )

    integration_type = fields.Selection(
        selection=[

        ],
        string='Integration Type',
        help='Type of integration for the connector',
    )





    def run(self, *args, **kwargs):
        """
        Run the integration process for the connector.
        This method should be overridden by specific connector implementations.
        """
        raise NotImplementedError("This method should be overridden in the specific connector implementation.")

