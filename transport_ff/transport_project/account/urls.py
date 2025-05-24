from django.urls import path
from . import views





urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('edit/', views.edit, name='profile-edit'),
    path('view_profile/', views.profile, name='profile'),
]