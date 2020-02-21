import requests.auth
import binascii
import hashlib
import hmac

class Client(requests.auth.AuthBase):
    def __init__(self, api_key, api_id):
        self.api_key = api_key.encode('utf-8')
        self.api_id = api_id
        self.api_url = 'https://api.unleashedsoftware.com'

    def get_query(self, url):
            parts = url.split('?')
            if len(parts) > 1:
                return parts[1]
            else:
                return ""

    def __call__(self, r):
        query = self.get_query(r.url)

        hashed = hmac.new(self.api_key, query.encode('utf-8'), hashlib.sha256)
        signature = binascii.b2a_base64(hashed.digest())[:-1]
        r.headers['api-auth-signature'] = signature
        r.headers['api-auth-id'] = self.api_id
        return r

    def _get_request(self, method, params=None):
        params = params or {}
        headers = {
            'content-type': 'application/json',
            'accept': 'application/json',
        }
        resp = requests.get(
            self.api_url + '/' + method,
            headers=headers,
            params=params,
            auth=self
        )
        return resp

    def request_endpoint(self, endpoint, options=None, page=None):
        if options is not None and page is not None:
            resp = self._get_request(endpoint + "/" + str(page) + "/" + "?" + options)
        elif options is not None and page is None:
            resp = self._get_request(endpoint + "?" + options)
        elif options is None and page is not None:
            resp = self._get_request(endpoint + "/" + str(page) + "/")
        else:
            resp = self._get_request(endpoint)
        json_parsed = resp.json()
        return json_parsed

    def return_items(self, endpoint ,options=None, page=None):
        return self.request_endpoint(endpoint,options,page)['Items']

    def return_pagination(self, endpoint ,options=None,page=None):
        return self.request_endpoint(endpoint,options,page)['Pagination']
