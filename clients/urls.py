from django.urls import path, include
from .views import *
from django.contrib import admin



urlpatterns = [

    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('sign-up/', TenantSignupView.as_view(), name="sign-up"),


]