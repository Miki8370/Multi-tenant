from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework import permissions
from .serializers import *
from  rest_framework.response import Response
from rest_framework import status
# Create your views here.

def index(request):
    return HttpResponse("home")


class TenantSignupView(APIView):
    #allowed_methods = ['get',]
    permission_classes = [permissions.AllowAny]
    serializer_class = TenantAccountSerailizer
    

    def post(self, request):
        serializer = TenantAccountSerailizer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Tenant account created successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

