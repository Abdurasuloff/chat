from django.urls import path
from .views import SignUpView  , profile ,  ProfileEditView, discover


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('edit/<str:username>/', ProfileEditView.as_view(), name=''),
    path('profile/<str:username>/', profile, name='user_detail'),
    path('discover', discover, name='discover'),
]