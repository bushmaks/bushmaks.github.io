from django import forms
from .models import SocialPlatform, CreatorProfile, Quote


class SocialPlatformForm(forms.ModelForm):
    class Meta:
        model = SocialPlatform
        exclude = ['id', 'creator']


class QuoteForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['offering', 'price']
