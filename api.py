import requests

class Api:

    def __init__(self, base=None):
        self.base_url = 'hasitdev.online/api/'
        if base is not None:
            self.base_url = base

    def getStatus(self, sub):
        r = requests.get('http://' + sub + '.' + self.base_url + 'status')
        if r.status_code is not 200:
            return 'Cannot find sub: ' + sub
        return r.json()['status']

    def update(self, sub, to):
        requests.put('http://' + sub + '.' + self.base_url + 'status/update/' + to)

    def create(self, sub):
        headers = {'Accept': 'application/json'}
        r = requests.post('http://' + self.base_url + 'subdomain', headers=headers, data = {'name':sub})
        if r.status_code is not 200:
            print r.text
            print r.status_code
            return 'Could not create sub: ' + sub
        return 'Success: created ' + sub
