from django.db import models
from strig.core.models import NamedModel
from django.utils.translation import ugettext as _

from strig.web.models.user import User

class AuditableNamedModel(NamedModel):    
    """
    AuditableNamedModel terá campos básicos para auditar os registros de uma entidade
    """
    creation_date = models.DateTimeField(
        _("Data de criação"), 
        auto_now=True,
        )

    modified_date = models.DateTimeField(
        _("Data de modificação"), 
        auto_now_add=True,
        )
    
    created_by = models.OneToOneField(
        User,
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_created_related",
        related_query_name="%(app_label)s_%(class)ss",
    )

    last_modified_by = models.OneToOneField(
        User,
        on_delete=models.DO_NOTHING,
        related_name="%(app_label)s_%(class)s_modified_related",
        related_query_name="%(app_label)s_%(class)ss",
    )

    class Meta:
        abstract=True

    def __str__(self):
        return self.name
