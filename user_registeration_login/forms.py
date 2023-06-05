from django import forms

class RegistrationForm(forms.Form):
    BUTTON_CHOICES = (
        ('New Registeration', 'register'),
        ('Already Registered', 'already registered'),
    )

    email = forms.EmailField()
    action = forms.ChoiceField(choices=BUTTON_CHOICES, widget=forms.RadioSelect)

class OTPForm(forms.Form):
    email = forms.EmailField()
    otp = forms.IntegerField()
