from django import forms

class RegistrationForm(forms.Form):

    email = forms.EmailField()

class OTPForm(forms.Form):
    email = forms.EmailField()
    otp = forms.IntegerField()
