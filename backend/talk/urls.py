from django.urls import path

from .views import TalkList, TalkDetail

urlpatterns = [
  path('', TalkList.as_view()),
  path('<pk>/', TalkDetail.as_view()),
]