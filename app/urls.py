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

from django.urls import path
from .views import Index, About, Gallery, Search
from django.template import loader
import os
from django.views.decorators.http import require_GET
from django.http import HttpResponse
from datetime import datetime
from api.models import Image
import json

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

@require_GET
def robots_txt(request):
    template = loader.get_template(os.path.join(BASE_DIR + '/templates/robots.txt'))
    return HttpResponse(template.render({}, request), content_type="text/html", charset="utf-8")

@require_GET
def sitemap_xml(request):
    template = loader.get_template(os.path.join(BASE_DIR + '/templates/sitemap.xml'))
    date = datetime.today().strftime('%Y-%m-%d')
    image = Image.objects.all()
    users =  []
    for x in range(0,len(image)):
        iuser = str(image[x].user)
        try:
            iuser = json.loads(iuser)
            if iuser['name'] not in users:
                users.append(iuser['name'])
        except Exception as e:
            if image[x].user not in users:
                users.append(image[x].user)

    context = {
    	'date': date,
        'users': users
    }
    return HttpResponse(template.render(context, request), content_type="text/xml", charset="utf-8")

urlpatterns = [
	path('', Index, name='index'),
	path('galeria/', Gallery.as_view(), name='gallery'),
	path('sobre/', About, name='about'),
    path('autor@/', Gallery.as_view(), name='search_gallery'),
    path('autor@/<str:author>/', Search.as_view(), name='search'),
	path('robots.txt', robots_txt),
	path('sitemap.xml', sitemap_xml),
]