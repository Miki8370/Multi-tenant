from django_tenants.middleware.main import TenantMainMiddleware

from django.http import HttpResponse
from django_tenants.utils import get_tenant_domain_model, get_public_schema_name

class CustomTenantMiddleware(TenantMainMiddleware):
    def process_request(self, request):
        try:
            super().process_request(request)
        except Exception as e:
            # Handle the case where no tenant is found for the hostname
            if request.get_host() == 'localhost':  # Match your public domain
                request.tenant = None
                request.schema_name = get_public_schema_name()  # Use public schema
            else:
                return HttpResponse(f"No tenant for hostname: {request.get_host()}", status=404)
