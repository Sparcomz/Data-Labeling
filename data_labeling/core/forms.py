from django import forms
from .models import User, Data

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

class RegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'role']
        widgets = {
            'password': forms.PasswordInput(),
        }

    ROLE_CHOICES = [
        ('uploader', 'Uploader'),
        ('annotator', 'Annotator'),
    ]
    role = forms.ChoiceField(choices=ROLE_CHOICES)

class DataUploadForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = ['data_type', 'task_type', 'task_description', 'text_content', 'image_content']
        widgets = {
            'task_description': forms.Textarea(attrs={'placeholder': 'Enter task description'}),
        }