from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import widgets
from main.models import Profile


class SignUpForm(UserCreationForm):

    first_name = forms.CharField(max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
    

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class EditProfileForm(UserChangeForm):

    username = forms.CharField(max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    is_active = forms.CharField(max_length=256, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    password = None

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_active')


class ProfilePageForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('bio', 'authorImage', 'instagram_url', 'linkedin_url', 'github_url', 'twitter_url', 'facebook_url', 'mail_id',)

        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            #'authorImage': forms.TextInput(attrs={'class': 'form-control'}),
            'instagram_url': forms.TextInput(attrs={'class': 'form-control'}),
            'linkedin_url': forms.TextInput(attrs={'class': 'form-control'}),
            'github_url': forms.TextInput(attrs={'class': 'form-control'}),
            'twitter_url': forms.TextInput(attrs={'class': 'form-control'}),
            'facebook_url': forms.TextInput(attrs={'class': 'form-control'}),
            'mail_id': forms.TextInput(attrs={'class': 'form-control'}),

        }