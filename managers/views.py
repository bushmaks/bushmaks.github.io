from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import Group
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from allauth.account.views import SignupView
from allauth.account.forms import SignupForm
from creators.models import Quote
from .models import BrandManagerProfile, Brand, Campaign
from .forms import BrandForm, CampaignForm


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


def brand_create(request):
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            brand = form.save(commit=False)
            brand.save()
            brand.managers.add(request.user.brandmanagerprofile)
            messages.success(request, 'Your brand has been added')
            return redirect('index')
    else:
        form = BrandForm()
    return render(request, 'managers/manager_form.html', {'form': form})


class BrandUpdateView(UpdateView):
    template_name = 'managers/manager_form.html'
    model = Brand
    fields = ['name', 'info']
    success_url = reverse_lazy('index')


class BrandDeleteView(DeleteView):
    template_name = 'managers/manager_confirm_delete.html'
    model = Brand
    success_url = reverse_lazy('index')


def campaign_create(request, pk):
    brand = Brand.objects.get(pk=pk)
    title = f'Create a Campaign for {brand.name}'
    if request.method == 'POST':
        form = CampaignForm(request.POST)
        if form.is_valid():
            campaign = form.save(commit=False)
            campaign.brand = brand
            campaign.save()
            messages.success(request, 'Your campaign has been posted')
            return redirect('index')
    else:
        form = CampaignForm()
    return render(request, 'managers/manager_form.html', {'form': form, "title": title})


class CampaignUpdateView(UpdateView):
    template_name = 'managers/manager_form.html'
    model = Campaign
    fields = ['name', 'goals', 'target_audience', 'detailed_description', 'niches', 'budget', 'submission_deadline']


class CampaignDeleteView(DeleteView):
    template_name = 'managers/manager_confirm_delete.html'
    model = Brand
    success_url = reverse_lazy('index')


def brand_detail(request, pk):
    brand = Brand.objects.get(pk=pk)
    campaigns = Campaign.objects.filter(brand=brand)
    return render(request, 'managers/brand_detail.html', {"brand": brand, "campaigns": campaigns})


class QuotesListView(ListView):

    def get_queryset(self):
        return Quote.objects.filter(campaign_id=campaign.id)
