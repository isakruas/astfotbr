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
import unicodedata
from django.contrib.auth.models import (
    BaseUserManager
)
from datetime import datetime
from django.conf import settings
from django.contrib.auth import password_validation
from django.contrib.auth.hashers import (
    check_password, is_password_usable, make_password,
)
from django.db import models
from django.utils.crypto import salted_hmac


class Image(models.Model):
    hash = models.CharField(unique=True,max_length=200, blank=False, null=False)
    user = models.CharField(max_length=200, blank=False, null=False)
    
    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
        ordering = ['id']

    def __str__(self):
        return self.hash


class Keyword(models.Model):
    name = models.CharField(unique=True,max_length=200, blank=False, null=False)
    
    class Meta:
        verbose_name = 'Keyword'
        verbose_name_plural = 'Keywords'
        ordering = ['id']

    def __str__(self):
        return self.name
