from django.contrib import admin
from django.urls import path, include

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/talks/', include('talk.urls')),
    path('api/users/', include('user.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-obtain/', obtain_jwt_token),
    path('api-token-refresh/', refresh_jwt_token),
    path('api-token-verify/', verify_jwt_token),
]
