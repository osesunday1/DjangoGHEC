from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import CreateView
from django.contrib import messages
from ghec_app.models import *
from ghec_app.forms import *
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import PasswordChangeForm
from django.urls import reverse_lazy


'''
class PasswordsResetView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('login')
    


def Login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user )
            return redirect ('clienthome')
        else:
            messages.success(request, ("there was an error logging in"))
            return redirect ('login')
    else:
        return render(request, 'registration/loginClient.html' )
'''    

def Login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            if user.is_admin or user.is_superuser:
                return redirect('adminhome')  # Redirect to the admin home page
            else:
                return redirect('clienthome')  # Redirect to the client home page
        else:
            messages.error(request, "There was an error logging in.")
            return redirect('login')
    else:
        return render(request, 'registration/loginClient.html')
    


def logout_user(request):
    logout(request)
    messages.success(request, ("You Are Logged Out"))
    return redirect ('home')



class ClientSignUpView(generic.CreateView):
    model = User
    form_class =ClientSignUpForm
    template_name = 'registration/signupClient.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'client'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


class AdminSignUpView(generic.CreateView):
    model = User
    form_class =AdminSignUpForm
    template_name = 'registration/signupAdmin.html'
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'admin'
        return super().get_context_data(**kwargs)
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')