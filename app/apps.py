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
from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
