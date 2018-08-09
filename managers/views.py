from django.shortcuts import render
from django.contrib.auth.models import Group
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from allauth.account.views import SignupView
from allauth.account.forms import SignupForm
from .models import BrandManagerProfile, Brand, Campaign
from creators.models import Quote


class BrandManagerSignupView(SignupView):
    template_name = 'account/managers_signup.html'
    form_class = SignupForm

    # group = Group.objects.get(id=1)

    def form_valid(self, form):
        response = super(BrandManagerSignupView, self).form_valid(form)
        user = self.user
        # self.group.user_set.add(user)
        BrandManagerProfile.objects.create(user=user)
        return response


class BrandCreateView(CreateView):
    model = Brand
    fields = ['name', 'info']


class BrandUpdateView(UpdateView):
    model = Brand
    fields = ['name', 'info']


class BrandDeleteView(DeleteView):
    model = Brand
    success_url = reverse_lazy('index')


class CampaignCreateView(CreateView):
    model = Campaign
    fields = ['name', 'brand', 'goals', 'target_audience', 'detailed_description', 'niches', 'budget',
              'submission_deadline']


class CampaignUpdateView(UpdateView):
    model = Campaign
    fields = ['name', 'goals', 'target_audience', 'detailed_description', 'niches', 'budget', 'submission_deadline']


class CampaignDeleteView(DeleteView):
    model = Brand
    success_url = reverse_lazy('')


class QuotesListView(ListView):

    def get_queryset(self):
        return Quote.objects.filter(campaign_id=campaign.id)
