from django.shortcuts import render
from django.contrib.auth.models import Group
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.urls import reverse_lazy
from allauth.account.views import SignupView
from allauth.account.forms import SignupForm
from .models import CreatorProfile, SocialPlatform, Quote
from .forms import SocialPlatformForm, QuoteForm


class CreatorSignupView(SignupView):
    template_name = 'account/creators_signup.html'
    form_class = SignupForm
    # group = Group.objects.get(id=2)

    def form_valid(self, form):
        response = super(CreatorSignupView, self).form_valid(form)
        user = self.user
        # self.group.user_set.add(user)
        CreatorProfile.objects.create(user=user)
        return response


class CreatorUpdateView(UpdateView):
    model = CreatorProfile
    fields = ['bio', 'niches', 'audience_demographic']


class PlatformCreateView(FormView):
    form_class = SocialPlatformForm


class PlatformUpdateView(UpdateView):
    model = SocialPlatform
    fields = ['account_name', 'url', 'metrics']
    success_url = reverse_lazy('index')


class PlatformDeleteView(DeleteView):
    model = SocialPlatform
    success_url = reverse_lazy('index')


class QuoteCreateView(FormView):
    template_name = 'creators/quote_form'
    form_class = QuoteForm


class QuoteUpdateView(UpdateView):
    model = Quote
    fields = ['offering', 'price']


class QuoteDeleteView(DeleteView):
    model = Quote
    success_url = reverse_lazy('index')