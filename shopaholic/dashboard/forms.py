from django import forms
from parsley.decorators import parsleyfy

from .models import UserInterest
from products.models import Brand, Category

@parsleyfy
class UserInterestForm(forms.ModelForm):
    GENDER_TYPE_CHOICES = (
        ('NA', 'Doesn\'t Matter',),
        ('MALE', 'Male',), ('FEMALE', 'Female',),
        ('BOY', 'Boy',), ('GIRL', 'Girl',),
    )
    email = forms.EmailField(
        required=False,
        widget=forms.TextInput(
            attrs={
                'id': "appendedInputButton",
                'class': "input-xxlarge c_email_enter_text",
                'placeholder': "enter your email address to stay updated!", })
    )
    interest = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        widget=forms.Select(
            attrs={'id': "c_hidden_input_one", })
    )
    brand = forms.ModelChoiceField(
        queryset=Brand.objects.all(),
        widget=forms.Select(
            attrs={'id': "c_hidden_input_two", })
    )
    gender_type = forms.CharField(widget=forms.Select(choices=GENDER_TYPE_CHOICES))

    class Meta:
        model = UserInterest