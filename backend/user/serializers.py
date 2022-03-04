from typing_extensions import Required
from rest_framework import serializers

from .models import User

class UserSerializer(serializers.ModelSerializer):
  id = serializers.UUIDField(read_only=True)
  password = serializers.CharField(write_only=True, required=False)
  is_staff = serializers.BooleanField(read_only=True, required=False)
  
  class Meta:
    model = User
    fields = ['id', 'email', 'name', 'password', 'is_staff', 'profile']
  
  def create(self, validated_data):
    return User.objects.create_user(request_data=validated_data)
  
  def update(self, instance, validated_data):
    # パスワードのみを変更する場合 or パスワード以外を変更する場合
    if 'password' in validated_data:
      # validated_dataにパスワードが含まれている場合は、パスワードをハッシュ化して格納
      instance.set_password(validated_data['password'])
    else:
      # パスワードが存在しない場合は、その他の更新情報をインスタンスに格納
      instance = super().update(instance, validated_data)
    instance.save()
    return instance