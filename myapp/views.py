from django.views import View
from django.shortcuts import render
from myapp.models import Product, MyUser, Purchase, Returns
from myapp.forms import NewUserCreationForm
from django.contrib.auth import login
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.db import transaction
from online_store import settings

def main(request):
    return render(request, 'main.html')

def purchase(request):
    return render(request, 'purchase.html')

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

class Login(LoginView):
    success_url = '/'
    template_name = 'login.html'

    def get_success_url(self):
        return self.success_url

class Register(CreateView):
    model = MyUser
    form_class = NewUserCreationForm
    success_url = '/'
    template_name = 'register.html'

    def form_valid(self, form):
        to_return = super().form_valid(form)
        login(self.request, self.object)
        msg = 'You have been successfully registered and logged in!'
        messages.success(self.request, msg)
        return to_return


class Logout(LoginRequiredMixin, LogoutView):
    next_page = '/'
    login_url = 'login/'

