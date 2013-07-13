from django import forms
from dashboard.models import UserInterest


class UserInterestForm(forms.ModelForm):

    class Meta:
        model = UserInterest