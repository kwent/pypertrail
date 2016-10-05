from .api import API
import requests


class System(API):

    def list(self):
        r = requests.get('{0}/{1}'.format(self.base_uri, 'systems.json'),
                         headers=self.headers)
        return self.return_response(r)

    def show(self, system_id):
        r = requests.get('{0}/{1}/{2}{3}'.format(self.base_uri,
                                                 'systems', system_id,
                                                 '.json'),
                         headers=self.headers)
        return self.return_response(r)

    def create(self, payload=None):
        r = requests.post('{0}/{1}'.format(self.base_uri, 'systems.json'),
                          headers=self.headers,
                          params=payload)
        return self.return_response(r)

    def update(self, system_id, payload=None):
        r = requests.put('{0}/{1}/{2}{3}'.format(self.base_uri,
                                                 'systems', system_id,
                                                 '.json'),
                         headers=self.headers,
                         params=payload)
        return self.return_response(r)

    def delete(self, system_id):
        r = requests.delete('{0}/{1}/{2}{3}'.format(self.base_uri,
                                                    'systems', system_id,
                                                    '.json'),
                            headers=self.headers)
        return self.return_response(r)

    def join_group(self, system_id, payload=None):
        r = requests.post('{0}/{1}/{2}/{3}'.format(self.base_uri,
                                                   'systems', system_id,
                                                   'join.json'),
                          headers=self.headers,
                          params=payload)
        return self.return_response(r)

    def leave_group(self, system_id, payload=None):
        r = requests.post('{0}/{1}/{2}/{3}'.format(self.base_uri,
                                                   'systems', system_id,
                                                   'leave.json'),
                          headers=self.headers,
                          params=payload)
        return self.return_response(r)
