

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from auth_.serializers import MainUserSerializer
from .models import MainUser


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    queryset = MainUser.objects.all()
    serializer_class = MainUserSerializer
    permission_classes = (AllowAny,)
