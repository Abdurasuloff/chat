
from . import views
from django.urls import path
urlpatterns = [
     path('chat/<str:username>' , views.chat, name="chat" ),
     path('data/<str:username>' , views.data, name="data" ),
     path('', views.friends, name='home'),
    
    
]
