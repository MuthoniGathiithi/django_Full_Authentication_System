from django.shortcuts import render,redirect
from .forms import SignUpForm
def signup_view(request):
    if request.method == 'POST':
        form=SignUpForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
        else:
            form=SignUpForm()
            return render(request,'signup.html',{'form':form})
        

# Create your views here.
