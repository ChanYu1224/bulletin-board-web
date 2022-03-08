from django.urls import path

from .views import TalkList, TalkCreate, TalkDetailRetrieve, TalkDetailEdit

urlpatterns = [
  path('list/', TalkList.as_view()),
  path('create/', TalkCreate.as_view()),
  path('<pk>/', TalkDetailRetrieve.as_view()),
  path('<pk>/edit/', TalkDetailEdit.as_view()),
]