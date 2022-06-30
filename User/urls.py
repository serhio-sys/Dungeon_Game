from django.urls import path
from .views import *

urlpatterns = [
 path('create/',CreateU.as_view(),name='reg'),
 path('login/',Auth.as_view(),name='login'),
 path('<pk>/',User.as_view(),name='user'),
 path('asdsa',Logout,name='logout')
]
