from .api import API
import requests


class Account(API):

    def list(self):
        r = requests.get('{0}/{1}'.format(self.base_uri, 'accounts.json'),
                         headers=self.headers)
        return self.return_response(r)
