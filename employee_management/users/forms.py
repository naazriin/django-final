from django import forms
from users.models import CustomUser
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(forms.ModelForm):
    
    class Meta:
        model = CustomUser
        fields = ['username','email', 'password']
