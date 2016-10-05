from .api import API
import requests


class SavedSearch(API):

    def list(self):
        r = requests.get('{0}/{1}'.format(self.base_uri, 'searches.json'),
                         headers=self.headers)
        return self.return_response(r)

    def show(self, saved_search_id):
        r = requests.get('{0}/{1}/{2}{3}'.format(self.base_uri,
                                                 'searches', saved_search_id,
                                                 '.json'),
                         headers=self.headers)
        return self.return_response(r)

    def create(self, payload=None):
        r = requests.post('{0}/{1}'.format(self.base_uri, 'searches.json'),
                          headers=self.headers,
                          params=payload)
        return self.return_response(r)

    def update(self, saved_search_id, payload=None):
        r = requests.put('{0}/{1}/{2}{3}'.format(self.base_uri,
                                                 'searches', saved_search_id,
                                                 '.json'),
                         headers=self.headers,
                         params=payload)
        return self.return_response(r)

    def delete(self, saved_search_id):
        r = requests.delete('{0}/{1}/{2}{3}'.format(self.base_uri,
                                                    'searches',
                                                    saved_search_id,
                                                    '.json'),
                            headers=self.headers)
        return self.return_response(r)
