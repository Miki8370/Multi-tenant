from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class TenantAccountSerailizer(serializers.Serializer):
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    schema_name = serializers.CharField(max_length=50)
    domain_name = serializers.CharField(max_length=255)
    business_type = serializers.ChoiceField(choices=[
        ('clothing', 'Clothing'),
        ('food', 'Food'),
        ('electronics', 'Electronics'),
    ], required=True)

    def create(self, validated_data):
        # Create the user
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )

        # Create the tenant
        tenant = Tenant.objects.create(
            schema_name=validated_data['schema_name'],
            name=f"Tenant for {user.username}",
            business_type=validated_data['business_type']
        )

        # Create the domain for the tenant
        Domain.objects.create(
            domain=validated_data['domain_name'],
            tenant=tenant,
            is_primary=True
        )

        return {
            "user": user,
            "tenant": tenant,
        }