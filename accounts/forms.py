
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    '''
    Extend UserCreationForm for Django with new fields of the abstracted user 
    '''
    is_technician = forms.BooleanField(initial=False, required=False)
    is_orderer = forms.BooleanField(initial=False, required=False)
    is_observer = forms.BooleanField(initial=False, required=False)

    class Meta(UserCreationForm):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("username", "is_technician", "is_orderer", "is_observer",)

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        if commit:
            user.save()
        return user

class CustomUserChangeForm(UserChangeForm):
    '''
    Extend UserChangeForm for Django with new fields of the abstracted user 
    '''
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields



class NewUserForm(UserCreationForm):
    '''
    UserCreationForm with added fields of the abstracted user for the front-end
    '''
    class Meta:
        model = CustomUser
        fields = (
            'username',
            'password1',
            'password2',
            'is_technician',
            'is_orderer',
            'is_observer'
        )
    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        if commit:
            user.save()
        return user
    