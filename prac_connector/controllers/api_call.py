from odoo import http, _



class PracConnectorApiCall(http.Controller):
    @http.route('/prac_connector/fetch_data', type='json', auth='user', methods=['POST'], csrf=False)
    def fetch_data(self, **kwargs):
        """
        Fetch data from external API and store it in prac.data.fetch model.
        """
        type = kwargs.get('type')
        date = kwargs.get('date')

        if type not in ['cnal', 'boc']:
            return {'error': _('Invalid type. Must be "cnal" or "boc".')}

        # Simulate fetching data from an external API
        fetched_data = f"Fetched data for type {type} on date {date}"

        # Create a new record in prac.data.fetch
        prac_data_fetch = http.request.env['prac.data.fetch'].create({
            'type': type,
            'date': date,
            'full_data': fetched_data,
            'data': fetched_data[:100],  # Store a snippet of the data
        })

        return {
            'message': _('Data fetched and stored successfully.'),
            'record_id': prac_data_fetch.id,
            'record_name': prac_data_fetch.name,
        }
