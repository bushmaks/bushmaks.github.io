from django.shortcuts import render
from django.contrib.auth.models import Group
from allauth.account.views import SignupView
from allauth.account.forms import SignupForm
from .models import CreatorProfile


class CreatorSignupView(SignupView):
    template_name = 'account/creators_signup.html'
    form_class = SignupForm
    group = Group.objects.get(id=2)

    def form_valid(self, form):
        response = super(CreatorSignupView, self).form_valid(form)
        user = self.user
        self.group.user_set.add(user)
        CreatorProfile.objects.create(user=user)
        return response
