from django import forms
from django.contrib.auth.models import User
from store1.models.Vendor import Vendor

class VendorForm(forms.ModelForm):

    username=forms.CharField(max_length=150,widget=forms.TextInput(attrs={
        'class': 'form-control','placeholder':'UserName ...'    }))
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={
              'class': 'form-control', 'placeholder': 'Email Address'        })    )
    
    password = forms.CharField( min_length=6, widget=forms.PasswordInput(attrs={
                    'class': 'form-control',   'placeholder': 'Password'     })    )


    class Meta:
        model=Vendor
        fields =['username','email','password','phone']
        widgets={
            'phone':forms.TextInput(attrs={
                'class': 'form-control',    'placeholder': 'Phone Number'      })        }
        
    def clean_username(self):
        username=self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('UserName already exists..')
        return username
    def clean_email(self):
        email=self.cleaned_data['email']

        if User.objects.filter(email=email):
            raise forms.ValidationError('Email already exists..')
        return email
    def clean_phone(self):
        phone=self.cleaned_data['phone']

        if not phone.isdigit():
            raise forms.ValidationError('phone numbers contain number not alphabets..')
        if len(phone) !=10:
            raise forms.ValidationError('Check phone number its not 10 digits ')
        return phone
