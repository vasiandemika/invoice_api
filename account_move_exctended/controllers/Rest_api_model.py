from odoo import http
from odoo.http import request, Response
import requests
import json



class RestApiModel(http.Controller):

    @http.route('/my_rest_api', type='json', auth='user', csrf=False, methods=['POST'])
    def index(self, **kw):

            print(kw)
            records = request.env['account.move'].sudo().create(kw)

            print(records.partner_id.name)
            data = {'success': True, 'move_id': records.id}
            return json.dumps(data), 200, {'content_type':'application/json;charset=utf-8'}




