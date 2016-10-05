from .api import API
import requests


class Group(API):

    def list(self):
        r = requests.get('{0}/{1}'.format(self.base_uri, 'groups.json'),
                         headers=self.headers)
        return self.return_response(r)

    def show(self, group_id):
        r = requests.get('{0}/{1}/{2}{3}'.format(self.base_uri,
                                                 'groups', group_id, '.json'),
                         headers=self.headers)
        return self.return_response(r)

    def update(self, group_id, payload={}):
        r = requests.put('{0}/{1}/{2}{3}'.format(self.base_uri,
                                                 'groups', group_id, '.json'),
                         headers=self.headers,
                         params=payload)
        return self.return_response(r)

    def delete(self, group_id):
        r = requests.delete('{0}/{1}/{2}{3}'.format(self.base_uri,
                                                    'groups', group_id,
                                                    '.json'),
                            headers=self.headers)
        return self.return_response(r)
