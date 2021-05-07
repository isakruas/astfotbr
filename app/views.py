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
from django.core import serializers
from django.views.generic import ListView, TemplateView
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from api.models import Image
import requests
import json
import random
from random import sample
from django.utils.safestring import mark_safe
from django.http import QueryDict


class Search(TemplateView):
	template_name = 'search.html'

	def get_context_data(self, **kwargs):
		context = super(Search, self).get_context_data(**kwargs)
		author = mark_safe(self.kwargs['author'])

		search = Image.objects.filter(user=author)

		if len(search) == 0:
			search_all = Image.objects.all()
			search = QueryDict('', mutable=True)
			key = 0
			for x in range(0,len(search_all)):
				if author in search_all[x].user:
					#search_all[x].user = json.loads(search_all[x].user)['name']
					search.setdefault(key, search_all[x])
					key += 1


		image = []

		for x in range(0,len(search)):
			ihash = str(search[x].hash)
			iuser = str(search[x].user)

			try:
				ihash = json.loads(ihash)
				iuser = json.loads(iuser)

				server = ihash['server']
				pid = ihash['id']
				secret = ihash['secret']

				owner = iuser['owner']
				name = iuser['name']

				el = {
					'user_name': f'{name}',
					'user_url': f'https://www.flickr.com/people/{owner}/',
					'photo_thumb': f'https://live.staticflickr.com/{server}/{pid}_{secret}.jpg',
					'photo_real': f'https://live.staticflickr.com/{server}/{pid}_{secret}_b.jpg',
				}
			except Exception as e:
				el = {
					'user_name': f'{iuser}',
					'user_url': f'https://www.astrobin.com/users/{iuser}/',
					'photo_thumb': f'https://www.astrobin.com/{ihash}/0/rawthumb/regular/',
					'photo_real': f'https://www.astrobin.com/{ihash}/',
				}

			image.append(el)

		context['search'] = image
		return context

class Gallery(ListView):
	template_name = 'gallery.html'
	model = Image
	paginate_by = 12
	ordering = 'id'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		image_list = context['image_list']
		image = []
		for x in range(0,len(image_list)):

			ihash = str(image_list[x].hash)
			iuser = str(image_list[x].user)

			try:
				ihash = json.loads(ihash)
				iuser = json.loads(iuser)

				server = ihash['server']
				pid = ihash['id']
				secret = ihash['secret']

				owner = iuser['owner']
				name = iuser['name']

				el = {
				 	'user_name': f'{name}',
				    'user_url': f'https://www.flickr.com/people/{owner}/',
				    'photo_thumb': f'https://live.staticflickr.com/{server}/{pid}_{secret}.jpg',
					'photo_real': f'https://live.staticflickr.com/{server}/{pid}_{secret}_b.jpg',
				}

			except Exception as e:

				el = {
				 	'user_name': f'{iuser}',
				    'user_url': f'https://www.astrobin.com/users/{iuser}/',
				    'photo_thumb': f'https://www.astrobin.com/{ihash}/0/rawthumb/regular/',
					'photo_real': f'https://www.astrobin.com/{ihash}/',
				}
			
			image.append(el)
		context['gallery'] = image
		return context

def Index(request):

	template = loader.get_template('index.html')

	image = []

	url_real = []

	ids = sample(range(1, len(Image.objects.all())), 10)

	for x in range(0,len(ids)):
		query = Image.objects.get(id=ids[x])

		ihash = str(query)
		iuser = str(query.user)

		try:
			ihash = json.loads(ihash)
			iuser = json.loads(iuser)

			server = ihash['server']
			pid = ihash['id']
			secret = ihash['secret']

			owner = iuser['owner']
			name = iuser['name']

			el = {
			 	'user_name': f'{name}',
			    'user_url': f'https://www.flickr.com/people/{owner}/',
			    'photo_thumb': f'https://live.staticflickr.com/{server}/{pid}_{secret}.jpg',
				'photo_real': f'https://live.staticflickr.com/{server}/{pid}_{secret}_b.jpg',
			}

		except Exception as e:

			el = {
			 	'user_name': f'{iuser}',
			    'user_url': f'https://www.astrobin.com/users/{iuser}/',
			    'photo_thumb': f'https://www.astrobin.com/{ihash}/0/rawthumb/regular/',
				'photo_real': f'https://www.astrobin.com/{ihash}/',
			}
		
		image.append(el)
 
	context = {
		'gallery': image
	}

	return HttpResponse(template.render(context, request), content_type='text/html', charset='utf-8')

def About(request):

	def f(n):
	    fat = 1
	    i = 2
	    while i <= n:
	        fat = fat*i
	        i = i + 1

	    return int(fat)

	template = loader.get_template('about.html')

	n = int(len(Image.objects.all()))
	p = 10

	c = int(f(n)/(f(p)*f(n-p)))

	context = {
		'c': c
	}

	return HttpResponse(template.render(context, request), content_type='text/html', charset='utf-8')
