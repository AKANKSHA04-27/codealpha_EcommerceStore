from django import forms

class CheckoutForm(forms.Form):
    """Form for collecting shipping information during checkout."""
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'First Name'
    }))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Last Name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control', 'placeholder': 'Email Address'
    }))
    phone = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Phone Number'
    }))
    address = forms.CharField(max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'Street Address'
    }))
    city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'City'
    }))
    state = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'State'
    }))
    zip_code = forms.CharField(max_length=20, widget=forms.TextInput(attrs={
        'class': 'form-control', 'placeholder': 'ZIP Code'
    }))
