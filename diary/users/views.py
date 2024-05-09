from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect('diary_list')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form':form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('diary_list')
            return redirect('diary_list')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form':form})

def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('diary_list')