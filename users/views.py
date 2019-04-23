from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm

def user_login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('login_success'))
        else:
            context["error"] = "Provide valid credentials !!"
            return render(request, "login.html", context)
    else:
        if not request.user.is_anonymous:
            return HttpResponseRedirect(reverse('login_success'))
        return render(request, "login.html", context)

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_login'))

def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login')
    else:
        form = UserCreationForm()
    return render(request, 'sign-up.html', {
        'form': form
    })
