from django import forms
from .models import LostItem, Report, User, Claim

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['item', 'reported_by', 'message', 'location_found']

    item = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Enter item name'}))
    reported_by = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Describe the issue...'}))
    location_found = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Location where found'}))

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class ClaimForm(forms.ModelForm):
    class Meta:
        model = Claim
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Explain why this item belongs to you...', 'rows': 3}),
        }

class LostItemForm(forms.ModelForm):
    class Meta:
        model = LostItem
        fields = ['item_name', 'description', 'location', 'date_lost', 'contact_info', 'status', 'image']
