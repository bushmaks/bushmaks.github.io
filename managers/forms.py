from django import forms
from .models import Brand, Campaign


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        exclude = ['managers']


class CampaignForm(forms.ModelForm):
    class Meta:
        model = Campaign
        exclude = ['id', 'posted', 'brand']
    submission_deadline = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
