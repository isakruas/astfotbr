"""
* Astrofotografia Brasil
* ======================
*
* Astrofotografia Brasil é uma plataforma para divulgação de astrofotografias feitas por
* profissionais e/ou amadores no território brasileiro, nesta perspectiva, objetiva incentivar
* a participação da comunidade brasileira em observações e registros de corpos celestes e
* fenômenos astronômicos.
*
* @author Isak Ruas
*
* @license Esta plataforma é disponibilizada sobre a Licença Pública Geral (GNU) V3.0
* Mais detalhes em: https://github.com/isakruas/astfotbr/blob/master/LICENSE
*
* @link Homepage: https://ast.fot.br/
* GitHub Repo: https://github.com/isakruas/astfotbr/
* README: https://github.com/isakruas/astfotbr/blob/master/README.md
*
* @version 1.0.30
"""

import json
try:
    import thread
except ImportError:
    import _thread as thread
import time
import requests
from urllib import parse

astrobin = {
    'api': '',
    'api_key': '',
    'api_secret': '',
}

flickr = {
    'api': '',
    'api_key': '',
    'api_secret': '',
}

astfotbr = {
    'api': 'https://ast.fot.br/api/v1/',
    'api_token': ''
}

keywords = []

limit = 20

offset = 0

image = []

image_buffer = []

def keyword():
    global keywords
    global astfotbr
    api = astfotbr['api']
    api_token = astfotbr['api_token'] 
    while True:
        try:
            response = requests.get(api+'keyword/').content.decode('utf-8')
            response = json.loads(response)
            response = response['results']
            keywords = []
            for x in range(0,len(response)):
                if response[x]['name'] not in keywords:
                    keywords.append(response[x]['name'])
        except Exception as e:
            pass
        time.sleep(1800)
        pass

def process():
    global image
    global astfotbr

    api = astfotbr['api']
    api_token = astfotbr['api_token'] 

    headers = {
        'Authorization': 'Token ' + api_token
    }
 
    while True:
        if len(image)>>0:

            data = {
                'hash': image[0]['hash'],
                'user': image[0]['user']
            }

            
            if isinstance(data['hash'], dict):
                data['hash'] = json.dumps(data['hash'])
                data['user'] = json.dumps(data['user'])
                try:
                    response = requests.post(url=api+'image/', data=data, headers=headers).content.decode('utf-8')
                    del(image[0])
                except Exception as e:
                    pass
            elif isinstance(data['hash'], str):
                try:
                    response = requests.post(url=api+'image/', data=data, headers=headers).content.decode('utf-8')
                    del(image[0])
                except Exception as e:
                    pass

        time.sleep(5)
        pass

def search_flickr(): 
    global flickr

    api = flickr['api']
    api_key = flickr['api_key'] 
    api_secret = flickr['api_secret']

    search  = {
        'method': 'flickr.photos.search',
        'api_key': api_key,
        'text': 'astfotbr',
        'privacy_filter': 1,
        'per_page': 1000,
        'format': 'json'

    }

    while True:

        parameters = parse.urlencode(search)
        url = api + '?' + parameters
        request = requests.get(url).content.decode('utf-8')
        request = json.loads(request[14:len(request)-1])
        if 'photos' in request:
            photos = request['photos']['photo']
            for x in range(0,len(photos)):
                photo = photos[x]
                owner = photo['owner']
                server = photo['server']
                pid = photo['id']
                secret = photo['secret']
                arguments = {
                    'method': 'flickr.people.getInfo',
                    'api_key': api_key,
                    'user_id': owner,
                    'format': 'json'
                }
                arguments = parse.urlencode(arguments)
                url = api + '?' + arguments
                request = requests.get(url).content.decode('utf-8')
                request = json.loads(request[14:len(request)-1])
                if 'person' in request:
                    user = request['person']['realname']['_content']
                    phash = {
                        'server': server,
                        'id': pid,
                        'secret': secret
                    }
                    puser = {
                        'owner': owner,
                        'name': user
                    }
                    if phash not in image_buffer:
                        obj = {
                            'hash': phash,
                            'user': puser
                        }
                        image.append(obj)
                        image_buffer.append(phash)                
                time.sleep(10)
        time.sleep(86400)

def search_astrobin():
    global keywords
    global astrobin
    global offset
    global limit
    global image
    global image_buffer

    api = astrobin['api']
    api_key = astrobin['api_key'] 
    api_secret = astrobin['api_secret'] 

    while True:
        if len(keywords)>>0:
            for x in range(0,len(keywords)):
                try:
                    query = keywords[x]
                    url = api + f'image/?limit={limit}&offset={offset}&description__icontains={query}&api_key='+api_key+'&api_secret='+api_secret
                    request = json.loads(requests.get(url).content.decode('utf-8'))
                    total_count = request['meta']['total_count']
                    offset = int(total_count/limit)
                    for y in range(1,(offset+1)):
                        url = api + f'image/?limit={limit}&offset={y}&description__icontains={query}&api_key='+api_key+'&api_secret='+api_secret
                        request = json.loads(requests.get(url).content.decode('utf-8'))
                        objects = request['objects']
                        for z in range(0,len(objects)):
                            if objects[z]['hash'] not in image_buffer:
                                obj = {
                                    'hash': objects[z]['hash'],
                                    'user': objects[z]['user']
                                }
                                image.append(obj)
                                image_buffer.append(objects[z]['hash'])
                except Exception as e:
                    pass
        image_buffer = []
        time.sleep(3600)
        pass

def main():
    thread.start_new_thread(keyword, ())
    time.sleep(10)
    thread.start_new_thread(search_flickr, ())
    time.sleep(10)
    thread.start_new_thread(search_astrobin, ())
    time.sleep(10)
    thread.start_new_thread(process, ())
    while True:
        time.sleep(3.154e+9)
        pass

if __name__ == '__main__':
    main()
