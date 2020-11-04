from django.db import models
from strig.web.models.utils import AuditableNamedModel
from django.utils.translation import ugettext as _

from .payment_tag import PaymentTag
from .payment_category import PaymentCategory

class PaymentType(models.TextChoices):
    UNKNOWN = 'UN', 'Desconhecido'
    DEBT = 'DE', 'Débito'
    CREDIT = 'CR', 'Crédito'

class Payment(AuditableNamedModel):
    payment_type = models.CharField(
        _("Tipo de pagamento (débito ou crédito)"), 
        max_length=2,
        choices=PaymentType.choices,
        default=PaymentType.UNKNOWN,
    )
    value = models.DecimalField(max_digits=9, decimal_places=2)
    payment_date = models.DateTimeField(_("Data do pagamento"))

    tag = models.ManyToManyField(PaymentTag, blank=True)
    category = models.ManyToManyField(PaymentCategory, blank=True)

    def __str__(self):
        return "{0} - {1}".format(self.name, self.value)