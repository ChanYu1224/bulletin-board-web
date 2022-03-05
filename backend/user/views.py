from rest_framework import generics
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response
from rest_framework import views

from django.http import Http404
from django.db import transaction

from .models import User
from .serializers import UserSerializer


class UserList(generics.ListAPIView):
  permission_classes = [permissions.IsAdminUser,]
  queryset = User.objects.all()
  serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
  permissions_classes = [permissions.IsAdminUser,]
  queryset = User.objects.all()
  serializer_class = UserSerializer


class UserRegister(generics.CreateAPIView):
  permission_classes = [permissions.AllowAny,]
  queryset = User.objects.all()
  serializer_class = UserSerializer

  @transaction.atomic
  def post(self, request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserOwnDetail(views.APIView):
  permission_classes = [permissions.IsAuthenticated,]
  queryset = User.objects.all()
  serializer_class = UserSerializer

  # GETメソッドでユーザ自身の情報を取得
  def get(self, request):
    response_data = {
      'name': request.user.name,
      'email': request.user.email,
      'profile': request.user.profile,
    }
    return Response(data=response_data, status=status.HTTP_200_OK)


class UserOwnUpdate(generics.UpdateAPIView):
  permission_classes = [permissions.IsAuthenticated,]
  queryset = User.objects.all()
  serializer_class = UserSerializer
  lookup_field = 'email'

  def get_object(self):
    try:
      instance = self.queryset.get(email=self.request.user)
      return instance
    except User.DoesNotExist:
      raise Http404


class UserOwnDelete(generics.DestroyAPIView):
  permission_classes = [permissions.IsAuthenticated,]
  queryset = User.objects.all()
  seriarizer_class = UserSerializer
  lookup_field = 'email'

  def get_object(self):
    try:
      instance = self.queryset.get(email=self.request.user)
      return instance
    except User.DoesNotExist:
      raise Http404