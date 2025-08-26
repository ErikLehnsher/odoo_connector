"""
wrapper for odoo requests
- retry
- handle error
- parse JSON
"""


import requests
import base64
from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
import logging


_logger = logging.getLogger(__name__)


class OdooConnectorRequest(models.Model):
    _name = 'odoo.connector.request'
    _description = 'Odoo Connector Request'


    config_id = fields.Many2one(
        string='Base Config',
        comodel_name='odoo.connector.base',
        required=True,
    )
    is_webhook = fields.Boolean(
        default=False,
    )
    method = fields.Selection(
        string='HTTP Method',
        selection=[
            ('GET', 'GET'),
            ('POST', 'POST'),
            ('PUT', 'PUT'),
            ('DELETE', 'DELETE'),
        ],
    )
    request_url = fields.Char(
        string='Request URL',
        help='Complete URL with all parameters.',
    )
    request_endpoint = fields.Char(
        string='Request Endpoint',
    )