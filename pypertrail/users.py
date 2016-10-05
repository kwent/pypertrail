from .api import API
import requests


class User(API):

    def list(self):
        r = requests.get('{0}/{1}'.format(self.base_uri, 'users.json'),
                         headers=self.headers)
        return self.return_response(r)

    def invite(self, payload=None):
        r = requests.get('{0}/{1}/{2}'.format(self.base_uri,
                                              'users', 'invite.json'),
                         headers=self.headers,
                         params=payload)
        return self.return_response(r)

    def delete(self, user_id):
        r = requests.delete('{0}/{1}/{2}{3}'.format(self.base_uri,
                                                    'users', user_id, '.json'),
                            headers=self.headers)
        return self.return_response(r)
