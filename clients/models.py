from django.db import models
from django_tenants.models import DomainMixin, TenantMixin
from django.contrib.auth.models import User
# Create your models here.

class Tenant(TenantMixin):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    """
      business_type = models.CharField(max_length=500, choices=[
        ('food', 'Food'),
        ('clothing', 'Clothing'),
    ])
    """

    created_at = models.DateTimeField(auto_now_add=True)


class Domain(DomainMixin):
    """def save(self, *args, **kwargs):
        if not self.domain:
            self.domain = f"{self.tenant.name}.localhost:8000"
        super().save(*args, **kwargs)  """

    is_primary = models.BooleanField(default=True)

