from os import name
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm , TextInput , EmailInput , FileInput , ModelForm, Textarea
from .models import CustomUser , feedback , coop

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ("username", "email")

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class feedback_form(ModelForm):
    class Meta:
        model = feedback
        fields = ['name', 'email' , 'phone' , 'adress' , 'text']
         
        widgets = {            
            "name": TextInput (attrs = { 'placeholder': 'NAME' , 'class': 'f1'}),
            "email": TextInput (attrs = { 'placeholder': 'EMAIL' , 'class': 'f1', 'type' : "email"}),
            "phone": TextInput (attrs = { 'placeholder': 'PHONE' , 'class': 'f1' }),  
            "adress": TextInput (attrs = { 'placeholder': 'ADRESS' , 'class': 'f1'}),  
            "text": Textarea(attrs={'placeholder': 'TEXT' , 'class': 'f1'}),      
            }
  
class order_form(ModelForm):
    class Meta:
        model = feedback
        fields = ['name', 'email' , 'phone' , 'adress' , 'text']
         
        widgets = {            
            "name": TextInput (attrs = { 'placeholder': 'NAME' , 'class': 'f1'}),
            "email": TextInput (attrs = { 'placeholder': 'Mail' , 'class': 'f1', 'type' : "email"}),
            "phone": TextInput (attrs = { 'placeholder': 'Phone' , 'class': 'f1' }),  
            "adress": TextInput (attrs = { 'placeholder': 'Address' , 'class': 'f1'}),  
            "text": Textarea(attrs={'placeholder': 'Message' , 'class': 'f1'}),        
            }        

class coop_form(ModelForm):
    class Meta:
        model = coop
        fields = ['org_name', 'site' , 'place' , 'activity' ,'adress' , 'name' , 'email', 'phone' , 'jt' , 'text']
         
        widgets = {            
            "org_name": TextInput (attrs = { 'placeholder': 'NAME' , 'class': 'f1'}),
            "site": TextInput (attrs = { 'placeholder': 'site' , 'class': 'f1'}),
            "place": TextInput (attrs = { 'placeholder': 'place' , 'class': 'f1' }),  
            "activity": TextInput (attrs = { 'placeholder': 'activity' , 'class': 'f1'}),  
            "adress": TextInput (attrs = { 'placeholder': 'adress' , 'class': 'f1'}),  
            "name": TextInput(attrs={'placeholder': 'name' , 'class': 'f1'}),    
            "email": TextInput (attrs = { 'placeholder': 'email' , 'class': 'f1'}),
            "phone": TextInput (attrs = { 'placeholder': 'phone' , 'class': 'f1', 'type' : "email"}),
            "jt": TextInput (attrs = { 'placeholder': 'jt' , 'class': 'f1' }),  
            "text": Textarea (attrs = { 'placeholder': 'text' , 'class': 'f1'}),     
            }