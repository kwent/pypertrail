import requests


class API:

    def __init__(self, token, debug=None):
        self.token = token
        self.base_uri = 'https://papertrailapp.com/api/v1'
        self.headers = {'X-Papertrail-Token': self.token}

        if debug:
            # Enabling debugging at http.client
            # level (requests->urllib3->http.client)
            # you will see the REQUEST, including HEADERS and DATA,
            # and RESPONSE with HEADERS but without DATA.
            # the only thing missing will be the response.body which is not
            # logged.
            try:  # for Python 3
                from http.client import HTTPConnection
            except ImportError:
                from httplib import HTTPConnection
            HTTPConnection.debuglevel = 1

    def return_response(self, response):
        if response.status_code == requests.codes.ok:
            return response.json()
        else:
            message = {'status_code': response.status_code}
            try:
                response.json()
                message.update(response.json())
            except:
                pass
            return message
