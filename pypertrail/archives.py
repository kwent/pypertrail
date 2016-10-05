from .api import API
import requests


class Archive(API):

    def list(self):
        r = requests.get('{0}/{1}'.format(self.base_uri, 'archives.json'),
                         headers=self.headers)
        return self.return_response(r)
