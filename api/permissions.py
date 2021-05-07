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
from rest_framework import permissions

methods = ('POST', 'PUT', 'PATCH', 'DELETE')


class ImagePermissions(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.method in methods:
            if not request.user.is_authenticated:
                return False

            return True

        return True

    def has_object_permission(self, request, view, obj):

        if request.method in methods:
            if not request.user.is_authenticated:
                return False

            return True

        return True


class KeywordPermissions(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.method in methods:
            if not request.user.is_authenticated:
                return False

            return True

        return True

    def has_object_permission(self, request, view, obj):

        if request.method in methods:
            if not request.user.is_authenticated:
                return False

            return True

        return True
