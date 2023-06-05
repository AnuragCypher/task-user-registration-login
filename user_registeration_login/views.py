from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils import timezone
from datetime import timedelta
from .models import CustomUser
from django.core.mail import send_mail
from .forms import RegistrationForm, OTPForm
import user_onboarding.settings as sp


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            if CustomUser.objects.filter(email=email).exists():

                if CustomUser.objects.get(email=email).verified:
                    request.session['redirected_from'] = sp.SESSION
                    return redirect('login')

            else:
                user = CustomUser(email=email)
                user.generate_otp()

                send_mail(
                    'OTP Verification',
                    f'Your OTP is: {user.otp}',
                    sp.EMAIL_HOST_USER,
                    [user.email],
                    fail_silently=False,
                )

                return redirect('otp_verification')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def otp_verification(request):
    if request.method == 'POST':
        form = OTPForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            otp = form.cleaned_data['otp']

            try:
                user = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                messages.error(request, 'Invalid Email for Further Processing')
                return redirect('otp_verification')
            print("user object", type(user))

            valid_otp = user.is_otp_valid()

            if valid_otp == True and str(user.otp) == str(otp):
                print("i am finally here to final response")
                user.verified = True
                user.save()
                messages.success(request, 'OTP verification successful.')
                request.session['redirected_from'] = sp.SESSION
                return redirect('login')

            messages.error(request, 'Invalid OTP., Either Entered OTP is Incorrect or Has Expired')
            return redirect('otp_verification')
    else:
        form = OTPForm()
    return render(request, 'otp_verification.html', {'form': form})


def login(request):
    if request.session.get('redirected_from') == sp.SESSION:
        return render(request, 'login.html')
    else:
        return render(request, 'warning.html')