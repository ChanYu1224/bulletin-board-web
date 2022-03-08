from django.shortcuts import get_object_or_404

from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError

from django_filters import rest_framework as filters

from .serializers import TalkSerializer, TalkSerializerIncludesUser
from .models import Talk


class TalkList(generics.ListAPIView):
  permission_classes = [permissions.IsAuthenticated,]
  queryset = Talk.objects.all()
  serializer_class = TalkSerializerIncludesUser


class TalkCreate(generics.CreateAPIView):
  permission_classes = [permissions.IsAuthenticated,]
  queryset = Talk.objects.all()
  serializer_class = TalkSerializer


class TalkDetailRetrieve(generics.RetrieveAPIView):
  permission_classes = [permissions.IsAuthenticated,]
  queryset = Talk.objects.all()
  serializer_class = TalkSerializerIncludesUser


class TalkDetailEdit(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = [permissions.IsAuthenticated,]
  queryset = Talk.objects.all()
  serializer_class = TalkSerializer