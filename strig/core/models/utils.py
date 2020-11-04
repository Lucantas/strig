from django.db import models
from django.utils.translation import ugettext as _

class NamedModel(models.Model):
    name = models.CharField(_("Nome"), max_length=80)
    description = models.TextField(_("Descrição"))
    
    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class OperationType(models.TextChoices):
    CREATE = 'CR', 'Criar'
    EDIT = 'ED', 'Editar'
    ENABLE = 'EN', 'Ativar'
    DISABLE = 'DI', 'Desativar'
    REMOVE = 'RM', 'Remover'
    