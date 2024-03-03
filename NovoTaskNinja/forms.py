from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'profile_picture', 'personal_info', 'dorm_preferences', 'major',
            'graduation_year', 'hometown', 'homestate', 'highschool', 'looking_for_roommate',
            'email', 'phone_number', 'snapchat', 'instagram'
        ]
        widgets = {
            'personal_info': forms.Textarea(attrs={'rows': 4}),
            'looking_for_roommate': forms.CheckboxInput(),
        }
        
# A profile search form from gpt
class ProfileSearchForm(forms.Form):
    query = forms.CharField(label='Search Profiles', max_length=100)
