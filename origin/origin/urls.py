from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token

from bonds.views import HelloWorld

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HelloWorld.as_view()),
    path('auth', obtain_auth_token),
    path('bonds/', include('bonds.urls')),
    path('users/', include('user.urls')),
]
