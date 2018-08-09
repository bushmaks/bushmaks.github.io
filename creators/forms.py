from django import forms
from .models import SocialPlatform, CreatorProfile, Quote


class SocialPlatformForm(forms.ModelForm):
    model = SocialPlatform
    fields = ['platform', 'account_name', 'url', 'metrics']


class QuoteForm(forms.ModelForm):
    model = Quote
    fields = ['offering', 'price']
