from django.urls import path
from .views import UserList, UserDetail, UserRegister, UserOwnDetail, UserOwnUpdate, UserOwnDelete

urlpatterns = [
  path('entire/', UserList.as_view()),
  path('entire/<pk>/', UserDetail.as_view()),
  path('register/', UserRegister.as_view()),
  path('myinfo/', UserOwnDetail.as_view()),
  path('update/', UserOwnUpdate.as_view()),
  path('delete/', UserOwnDelete.as_view()),
]