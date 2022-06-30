from django.urls import path
from .views import *

urlpatterns = [
 path('create/',CreateU.as_view(),name='reg'),
 path('login/',Auth.as_view(),name='login'),
 path('',User.as_view(),name='userq'),
 path('asdsa/',Logout,name='logout'),
 path('<pk>/',UserDetail.as_view(),name='user'),
 path('<pk>/delete/',DeleteUSer.as_view(),name='del'),
]
