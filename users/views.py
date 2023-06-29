from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages


def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registered successfully!")
            return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)


def logout(request):
    logout(request)
    return redirect('home')
