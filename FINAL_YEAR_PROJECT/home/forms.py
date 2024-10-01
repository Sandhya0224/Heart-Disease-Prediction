from django import forms 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm

class UserCreationform(UserCreationForm):
    def __init__(self,*args,**kwargs):
        super(UserCreationform,self).__init__(*args,*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-red-500 focus:bg-white focus:ring-2 focus:ring-red-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'
        }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class':'w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-red-500 focus:bg-white focus:ring-2 focus:ring-red-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'
        }))

    password1 = forms.CharField(widget = forms.PasswordInput(attrs={
        'class':'w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-red-500 focus:bg-white focus:ring-2 focus:ring-red-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'
    }))

    password2 = forms.CharField(widget = forms.PasswordInput(attrs={
        'class':'w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-red-500 focus:bg-white focus:ring-2 focus:ring-red-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'
    }))


class Authenticationform(AuthenticationForm):
    def __init__(self,*args,**kwargs):
        super(Authenticationform,self).__init__(*args,*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(attrs={
        'class':'w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-red-500 focus:bg-white focus:ring-2 focus:ring-red-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'
        }))
    password = forms.CharField(widget = forms.PasswordInput(attrs={
        'class':'w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-red-500 focus:bg-white focus:ring-2 focus:ring-red-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out'
    }))