from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

from django.shortcuts import render, redirect, reverse
from django.utils.encoding import force_bytes, force_text
from django.views import View
from django.core.mail import send_mail

from .forms import SignUpForm

sign_up_html = 'signup.html'

class RegisterView(View):
    def get(self, request):
        return render(request, sign_up_html, { 'form': SignUpForm() })

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            #user = form.save()
            #return redirect(reverse('login'))
            form.save()
            messages.info(request, "Thanks for registering. You are now logged in.")
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)
            
            send_mail(
                'Account sign up for Pancake Ride',
                'Congratulation! You have successfully signed up for Pnacake Ride.\n Your username is: ' + new_user.username + ' Your password is: ' + form.cleaned_data['password1'] + '.\n',
                'Pancake Ride',
                [form.cleaned_data['email']],
                fail_silently=False,
            )
            
            return redirect(reverse('login'))

        return render(request, sign_up_html, { 'form': form })


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')