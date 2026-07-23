from django import forms
from store1.models import Customer


class CustomerForm(forms.ModelForm):
    
    class Meta:
        model=Customer
        fields="__all__"
        widgets = {
            'password': forms.PasswordInput()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control'
            })

        self.fields['first_name'].widget.attrs['placeholder'] = 'First Name'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Last Name'
        self.fields['phone'].widget.attrs['placeholder'] = 'Phone Number'
        self.fields['email'].widget.attrs['placeholder'] = 'Email Address'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'

  
    def clean_phone(self):
        phone=self.cleaned_data['phone']
        if len(phone)!=10:
             raise forms.ValidationError("Phone Number Must Be 10 Digits")
        if not  phone.isdigit():
            raise forms.ValidationError('Phone Number Should Contain Only number ')
        return phone
        
    def clean_password(self):
        password=self.cleaned_data['password']

        if len(password) < 6:
                raise forms.ValidationError("Password must be at least 6 characters.")
        return password

