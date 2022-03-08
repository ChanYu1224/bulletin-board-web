from rest_framework import serializers
from .models import Talk
from user.serializers import UserSerializer

class TalkSerializerIncludesUser(serializers.ModelSerializer):
  send_by = UserSerializer()

  class Meta:
    model = Talk
    fields = '__all__'


class TalkSerializer(serializers.ModelSerializer):
  class Meta:
    model = Talk
    fields = '__all__'