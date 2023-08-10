from django import forms
from .models import Phone

class AddPhoneForm(forms.ModelForm):

    class Meta:
        model = Phone
        fields = "__all__"