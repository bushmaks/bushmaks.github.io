from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.BrandManagerSignupView.as_view(), name='managers_signup'),
]
