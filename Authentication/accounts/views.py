from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def signup_view(request):
    success_message = None
    error_message = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            from django.contrib.auth.models import User
            if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
                error_message = 'User already signed up.'
            else:
                user = form.save(commit=False)
                user.set_password(form.cleaned_data['password'])
                user.save()
                success_message = 'Account created successfully! You can now log in.'
                form = SignUpForm()  # Reset the form after success
        # else: errors will be shown by form.errors
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form, 'success_message': success_message, 'error_message': error_message})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')        
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    return render(request, 'accounts/login.html')

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')



