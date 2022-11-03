from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Account
from .forms import SingupForm

def login(request):
    return render(request, 'accounts/login.html')

# def signup(request):
#     if request.method == 'POST':
#         firstname = request.POST.get('firstname')
#         lastname = request.POST.get('lastname')
#         email = request.POST.get('email')
#         password = request.POST.get('password')

#         account = Account
#         account.first_name = firstname
#         account.last_name = lastname
#         account.email = email
#         account.username = email
#         account.password = password

#         context = {}
#         return render(request, 'accounts/signup.html', context)
#     return render(request, 'accounts/signup.html')

def signup(request):
    if request.method == 'POST':
        form = SingupForm(request.POST)
        print(form)
        if form.is_valid():
            return redirect('login')

        return HttpResponse(0)
    else:
        form = SingupForm()

    return render(request, 'accounts/signup.html', {'form': form})
