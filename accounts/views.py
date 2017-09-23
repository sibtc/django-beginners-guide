from django.contrib.auth import update_session_auth_hash, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect

from .forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def change_password(request):
    '''
    Updating a user's password logs out all sessions for the user.
    After saving the form, call the `update_session_auth_hash`
    function to avoid logging out the user.
    '''
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('change_password')  # redirect to avoid re-submission
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})
