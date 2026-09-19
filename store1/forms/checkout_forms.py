from django import forms


class CheckoutForm(forms.Form):

    address = forms.CharField(
        max_length=250,
        required=True,
        widget=forms.Textarea(attrs={
            'rows': 4,
            'placeholder': 'House/Flat No, Street, Area'
        })
    )

    city = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter city'
        })
    )

    state = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter state'
        })
    )

    pincode = forms.CharField(
        max_length=6,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter 6-digit pincode'
        })
    )

    phone = forms.CharField(
        max_length=10,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter 10-digit mobile number'
        })
    )

    latitude = forms.DecimalField(
        required=False
    )

    longitude = forms.DecimalField(
        required=False
    )

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        for field in self.fields.values():

            field.widget.attrs.update({
                'class': 'form-control'
            })

    def clean_phone(self):

        phone = self.cleaned_data['phone']

        if not phone.isdigit():
            raise forms.ValidationError(
                "Phone number should contain only digits."
            )

        if len(phone) != 10:
            raise forms.ValidationError(
                "Phone number must be exactly 10 digits."
            )

        return phone

    def clean_pincode(self):

        pincode = self.cleaned_data['pincode']

        if not pincode.isdigit():
            raise forms.ValidationError(
                "Pincode should contain only digits."
            )

        if len(pincode) != 6:
            raise forms.ValidationError(
                "Pincode must be exactly 6 digits."
            )

        return pincode

    def clean_address(self):

        address = self.cleaned_data['address'].strip()

        if len(address) < 10:
            raise forms.ValidationError(
                "Please enter a complete delivery address."
            )

        return address