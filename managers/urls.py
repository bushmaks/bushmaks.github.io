from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.BrandManagerSignupView.as_view(), name='managers_signup'),
    path('brands/new/', views.brand_create, name='brand_create'),
    path('brands/update/<pk>/', views.BrandUpdateView.as_view(), name='brand_update'),
    path('brands/delete/<pk>/', views.BrandDeleteView.as_view(), name='brand_delete'),
    path('brands/details/<pk>/', views.brand_detail, name='brand_detail'),
    path('brands/campaigns/<pk>/', views.brand_campaigns, name='brand_campaigns'),
    path('campaigns/new/<pk>/', views.campaign_create, name='campaign_create'),
    path('campaigns/update/<pk>/', views.CampaignUpdateView.as_view(), name='campaign_update'),
    path('campaigns/delete/<pk>/', views.CampaignDeleteView.as_view(), name='campaign_delete'),
    path('campaigns/quotes/<pk>/', views.campaign_quotes, name='campaign_quotes'),
    path('quotes/accept/<pk>/', views.accept_quotes, name='accept_quotes'),
]
