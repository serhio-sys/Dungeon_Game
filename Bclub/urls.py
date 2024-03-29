"""Bclub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('game/',include('Game.urls')),
    path('',HomePage.as_view(),name='home'),
    path('img/<pk>/',UpdatePhoto.as_view(),name='upd'),
    path('registationotlogin/',Registr.as_view(),name='logorreg'),
    path('users/', AllUsers.as_view(),name='users'),
    path('user/',include('User.urls')),
    re_path(r'^media/(?P<path>.*)$',serve, {'document_root': settings.MEDIA_ROOT}),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns() 
