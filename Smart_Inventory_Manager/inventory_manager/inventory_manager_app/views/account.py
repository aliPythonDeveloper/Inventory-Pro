from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render  # Make sure to import render here
from ..decorator.decorator import *

@unauthenticated_user
def loginUser(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        print("USERNAME", username)
        print("PASSWORD", password)
        user = authenticate(request, username=username, password= password)

        if user is not None:
            login(request, user)
            return redirect('inventory_manager_app:home')
        else:
            messages.info(request, 'Username OR Password is incorrect')

    context = {}
    return render(request, 'account/login1.html', context)

def logoutUser(request):
    logout(request)
    return redirect('inventory_manager_app:login')

class loginType(TemplateView):
    template_name = 'account/login_type.html'