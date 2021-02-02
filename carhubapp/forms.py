from django import forms
from . models import Profile, Comments, Post
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class PostImagesForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'date',]


class PostComments(forms.ModelForm):
    class Meta: 
        model = Comments
        exclude = ['image','posted','user']
        
class PostProfile(forms.ModelForm):
    class Meta:
        models = Profile
        exclude = ['user',]
        
class UpdateUserProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'profile_picture', 'bio']
        
        
class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name', max_length=30)
    email = forms.EmailField(label='Email')                                                                                    

    
class SignUpForm(UserCreationForm):
    email = forms.EmailField(help_text='Enter Email!')
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
