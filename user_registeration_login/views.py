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
                existing_user = CustomUser.objects.filter(email=email)[0]
                existing_user.generate_otp()

                send_mail(
                    'OTP Verification',
                    f'Your OTP is: {existing_user.otp}',
                    sp.EMAIL_HOST_USER,
                    [existing_user.email],
                    fail_silently=False,
                )

                return redirect('otp_verification')

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
            print(valid_otp)
            print(user.otp)
            print(otp)

            if valid_otp == True and str(user.otp) == str(otp):
                print("i am finally here to final response")
                # user.otp = None
                # user.otp_created_at = None
                # user.save()
                messages.success(request, 'OTP verification successful.')
                # request.session['redirected_from'] = sp.SESSION
                return redirect('login')

            messages.error(request, 'Invalid OTP.')
            return redirect('otp_verification')
    else:
        form = OTPForm()
    return render(request, 'otp_verification.html', {'form': form})


def login(request):
    # if request.session.get('redirected_from') == sp.SESSION:
    return render(request, 'login.html')
    # else:
    #     return render(request, 'warning.html')