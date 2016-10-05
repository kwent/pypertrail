from .api import API
import requests


class Search(API):

    def __init__(self, token, debug=None):
        API.__init__(self, token, debug)
        self.min_id = None
        self.max_id = None

    def return_response(self, response):
        if response.status_code == requests.codes.ok:
            r = response.json()
            self.min_id = r['min_id']
            self.max_id = r['max_id']
            return response.json()
        else:
            message = {'status_code': response.status_code}
            try:
                response.json()
                message.update(response.json())
            except:
                pass
            return message

    def events(self, query=None, system_id=None, group_id=None,
               min_id=None, min_time=None, max_id=None, max_time=None,
               follow=False, delay=None):

        params = {'q': query,
                  'system_id': system_id,
                  'group_id': group_id,
                  'min_id': min_id,
                  'min_time': min_time,
                  'max_id': max_id,
                  'max_time': max_time}

        if follow:
            params['tail'] = 'true'
            if self.min_id:
                params['max_id'] = self.min_id

        r = requests.get('{0}/{1}/{2}'.format(self.base_uri,
                                              'events', 'search.json'),
                         headers=self.headers,
                         params=params)

        return self.return_response(r)
