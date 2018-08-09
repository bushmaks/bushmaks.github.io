from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.BrandManagerSignupView.as_view(), name='managers_signup'),
    path('brands/new/', views.BrandCreateView.as_view(), name='brand_create'),
    path('brands/update/<pk>/', views.BrandUpdateView.as_view(), name='brand_update'),
    path('brands/delete/<pk>/', views.BrandDeleteView.as_view(), name='brand_delete'),
    path('campaigns/new/', views.CampaignCreateView.as_view(), name='campaign_create'),
    path('campaigns/update/<pk>/', views.CampaignCreateView.as_view(), name='campaign_create'),
    path('campaigns/delete/<pk>/', views.CampaignCreateView.as_view(), name='campaign_create'),
]
