from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.CreatorSignupView.as_view(), name='creators_signup'),
]
