from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import *
from django.forms import ModelForm






class ClientSignUpForm(UserCreationForm):  
    first_name=forms.CharField(required=True, widget = forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(required=True, widget = forms.TextInput(attrs={'class':'form-control'}))
    phone = forms.CharField(required=True, widget = forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(required=False, widget = forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta(UserCreationForm.Meta):
        model = User
        #fields = "__all__"
        fields = ('email', 'password1', 'password2','first_name', 'last_name', 'phone', 'address')
    @transaction.atomic
    def save(self):
        
        user = super().save(commit=False)
        
        user.is_client = True
        user.save()
        client = Client.objects.create(user=user)
        client.first_name=self.cleaned_data.get('first_name')
        client.last_name=self.cleaned_data.get('last_name')
        client.phone=self.cleaned_data.get('phone')
        client.address=self.cleaned_data.get('address')
        client.save()
        return user
    
    def __init__(self, *args, **kwargs):
        super(ClientSignUpForm, self). __init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'



class DateInput(forms.DateInput):
    input_type = 'date'

class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields= ('client_name', 'country', 'package') 
        widgets= {
            'client_name': forms.TextInput(attrs={'class':'form-control', 'value': '', 'id':'elder', 'type':'hidden'}),
            #'client_name': forms.Select(attrs={'class':'form-control', 'placeholder': 'what is your name'}),
            'country': forms.Select(attrs={'class':'form-control'}),
            'package': forms.Select(attrs={'class':'form-control'}),
            #'date': DateInput(attrs={'type': 'date', 'class':'form-control', 'placeholder': 'Tell us the date'}),
        }



class ApplicationForm2(ModelForm):
    class Meta:
        model = Application
        fields= ('client_name', 'country', 'package', 'processing_fee', 'amount_paid','debt','ielts') 
        widgets= {
            'client_name': forms.Select(attrs={'class':'form-control'}),
            'country': forms.Select(attrs={'class':'form-control'}),
            'package': forms.Select(attrs={'class':'form-control'}),
            'processing_fee': forms.TextInput(attrs={'class':'form-control'}),
            'amount_paid': forms.TextInput(attrs={'class':'form-control'}),
            'debt': forms.TextInput(attrs={'class':'form-control'}),
            'ielts': forms.CheckboxInput(),
        }





class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields= ('first_name','last_name', 'phone', 'address') 
        widgets= {
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'phone': forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
        }



class ReceiptForm(ModelForm):
    class Meta:
        model = Receipt
        fields= ('client_name', 'amount_paid', 'sender_name', 'date_paid', 'bank_name','reason') 
        widgets= {
            'client_name': forms.Select(attrs={'class':'form-control', 'placeholder': "client name"}),
            'amount_paid': forms.TextInput(attrs={'class':'form-control', 'placeholder': "amount paid"}),
            'sender_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': "name of sender"}),
            'date_paid': DateInput(attrs={'type': 'date', 'class':'form-control', 'placeholder': 'Tell us the date'}),
            'bank_name': forms.TextInput(attrs={'class':'form-control', 'placeholder': "bank name"}),
            'reason': forms.Select(attrs={'class':'form-control', 'placeholder': "reason"}),
  
        }




class AdminSignUpForm(UserCreationForm):  
    first_name=forms.CharField(required=True, widget = forms.TextInput(attrs={'class':'form-control'}))
    last_name=forms.CharField(required=True, widget = forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta(UserCreationForm.Meta):
        model = User
        #fields = "__all__"
        fields = ('email', 'password1', 'password2','first_name', 'last_name')
    @transaction.atomic
    def save(self):
        
        user = super().save(commit=False)
        
        user.is_admin = True
        user.save()
        admin = Admin.objects.create(user=user)
        admin.first_name=self.cleaned_data.get('first_name')
        admin.last_name=self.cleaned_data.get('last_name')
        admin.save()
        return user
    
    def __init__(self, *args, **kwargs):
        super(AdminSignUpForm, self). __init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'