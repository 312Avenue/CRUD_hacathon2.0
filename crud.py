import json
import requests
from settings import settings


class CRUD:

    def check_id(self, id_, req):
        for i in req['records']:
            if id_ == i['id']:
                return i
        return False

    def create(self):
        print('Create')
        obj = json.dumps({'records': [
            {'fields': {
                'Marka':        input('Marka: '), 
                'Model':        input('Model: '), 
                'Year':         int(input('year: ')),
                'Volume':       float(input('Volume: ')),
                'Color':        input('color: '),
                'Machine type': input('machine type: ').capitalize(),
                'km':           int(input('km: ')),
                'Price':        float(input('price: '))
                }}
            ]})
        print(obj)
        req = requests.post(
            settings.get_url,
            headers=settings.AUTH_TOKEN_HEADER_FOR_CREATE, 
            data=obj)
        return req.json()

    
    def listining(self):
        req = requests.get(settings.get_url, headers=settings.AUTH_TOKEN_HEADER)
        return req.json().get('records')


    def retrieve(self, id_):
        req = requests.get(settings.get_url, headers=settings.AUTH_TOKEN_HEADER).json()
        if self.check_id(id_, req):
            return self.check_id(id_, req)
        else:
            return 'Not found'


    def update(self, id_):
        print('Update')
        req = requests.get(settings.get_url, headers=settings.AUTH_TOKEN_HEADER_FOR_CREATE).json()
        if self.check_id(id_=id_, req=req):
            obj = json.dumps(
            {'fields': {
                'Marka':        input('Marka: '), 
                'Model':        input('Model: '), 
                'Year':         int(input('year: ')),
                'Volume':       float(input('Volume: ')),
                'Color':        input('color: '),
                'Machine type': input('machine type: ').capitalize(),
                'km':           int(input('km: ')),
                'Price':        float(input('price: '))
                }}
            )
            req = requests.patch(
                settings.get_url + f'/{id_}',
                headers=settings.AUTH_TOKEN_HEADER_FOR_CREATE, 
                data=obj)
            return req.json()
        else:
            return 'Not found'

    
    def delete(self, id_):
        req = requests.get(settings.get_url, headers=settings.AUTH_TOKEN_HEADER).json()
        if self.check_id(id_=id_, req=req):
            req = requests.delete(settings.get_url + f'/{id_}', headers=settings.AUTH_TOKEN_HEADER)
            return req.text
        else:
            return 'Not found'
        


crud = CRUD()
