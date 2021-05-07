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
from rest_framework.routers import SimpleRouter
from .views import (
    ImageViewSet,
    KeywordViewSet
)

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

router = SimpleRouter()
router.register('api/v1/image', ImageViewSet)
router.register('api/v1/keyword', KeywordViewSet)
urlpatterns = []
urlpatterns += router.urls
