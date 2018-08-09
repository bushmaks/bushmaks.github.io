from django import forms
from .models import Brand, Campaign


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        exclude = ['managers']


class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        exclude = ['posted']
