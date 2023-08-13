from django import forms
from .models import Phone

class AddPhoneForm(forms.ModelForm):

    class Meta:
        model = Phone
        fields = "__all__"
        
#we also can write serializers.py instead of forms.py if we want to use rest_framework.        