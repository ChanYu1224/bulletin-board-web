from django.shortcuts import get_object_or_404

from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError

from django_filters import rest_framework as filters

from .serializers import TalkSerializer
from .models import Talk


class TalkFilter(filters.FilterSet):
  class Meta:
    model = Talk
    fields = '__all__'


class TalkList(views.APIView):
  # admin画面でフォームを表示するためにシリアライザを代入
  serializer_class = TalkSerializer

  def post(self, request):
    # request.dataからリクエストデータを取得
    serializer = TalkSerializer(data=request.data)
    # バリデーション
    serializer.is_valid(raise_exception=True)
    # モデルオブジェクトとして保存
    serializer.save()

    return Response(serializer.data, status.HTTP_201_CREATED)

  def get(self, request):
    # request.queryparamsで直接クエリ文字列を取得
    filterset = TalkFilter(request.query_params, queryset=Talk.objects.all())
    # バリデーション
    if not filterset.is_valid():
      ValidationError(filterset.errors)
    # filtersetで既にバリデーションを済ませているから、直接インスタンスに代入
    serializer = TalkSerializer(instance=filterset.qs, many=True)

    return Response(serializer.data, status.HTTP_200_OK)


class TalkDetail(views.APIView):
  # admin画面でフォームを表示するためにシリアライザを代入
  serializer_class = TalkSerializer

  def get(self, request, pk):
    # モデルからpkに該当するオブジェクトを取得
    talk = get_object_or_404(Talk.objects.all(), pk=pk)
    # モデルオブジェクトをインスタンスに代入
    serializer = TalkSerializer(instance=talk)
    # モデルに格納されているデータのためバリデーションせずにそのまま返すことが出来る
    return Response(serializer.data, status.HTTP_200_OK)

  def put(self, request, pk):
    # モデルからpkに該当するオブジェクトを取得
    talk = get_object_or_404(Talk.objects.all(), pk=pk)
    # instanceにモデルオブジェクト、dataにリクエストデータ
    serializer = TalkSerializer(instance=talk, data=request.data)
    # バリデーション
    serializer.is_valid(raise_exception=True)
    # モデルオブジェクトを更新
    serializer.save()

    return Response(serializer.data, status.HTTP_200_OK)

  def patch(self, request, pk):
    #モデルからpkに該当するオブジェクトを取得
    talk = get_object_or_404(Talk.objects.all(), pk=pk)
    #instanceにモデルオブジェクト、dataにリクエストデータを代入、一部更新であるためpartial=True
    serializer = TalkSerializer(instance=talk, data=request.data, partial=True)
    #バリデーション
    serializer.is_valid(raise_exception=True)
    #モデルオブジェクトを更新
    serializer.save()

    return Response(serializer.data, status.HTTP_200_OK)

  def delete(self, request, pk):
    #モデルからpkに該当するオブジェクトを取得
    talk: Talk = get_object_or_404(Talk.objects.all(), pk=pk)
    #モデルからオブジェクトを削除
    talk.delete()

    return Response(status=status.HTTP_204_NO_CONTENT)