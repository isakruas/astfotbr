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

from rest_framework import mixins
from rest_framework import viewsets
from .models import (
    Image,
    Keyword
)
from .serializers import (
    ImageSerializer,
    KeywordSerializer
)
from .permissions import (
    ImagePermissions,
    KeywordPermissions
)


class ImageViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet):
    """API Image V1.0.0"""

    permission_classes = (ImagePermissions,)

    queryset = Image.objects.all()
    serializer_class = ImageSerializer


class KeywordViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet):
    """API Keyword V1.0.0"""

    permission_classes = (KeywordPermissions,)

    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer