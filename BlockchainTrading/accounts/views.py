from django.contrib.auth import forms as auth_forms
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import views as auth_views, get_user_model
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from BlockchainTrading.accounts.forms import UserCreateForm

# Create your views here.

# authenticate(request, **credentials) -> returns the user if credentials match
# login(request, user) -> attaches a cookie for the authenticated user

# correct way of importing user is:
UserModel = get_user_model()


# in the settings.py, add configuration AUTH_USER_MODEL = 'accounts/AppUSer'

class LoginUserView(auth_views.LoginView):
    template_name = 'account/login_user.html'

    # def get_success_url(self):
    #     return reverse_lazy('dashboard')

    # if next is not provided, it should redirect to dashboard, tfore in settings.py =>
    # LOGIN_REDIRECT_URL = reverse_lazy('dashboard)


class RegisterUserView(CreateView):
    # form_class = auth_forms.UserCreationForm  # default form in Django for user creation
    form_class = UserCreateForm  # default form in Django for user creation
    template_name = 'account/register_user.html'
    success_url = reverse_lazy('dashboard')  # must login at same time


class LogoutUserView(auth_views.LogoutView):
    def get_success_url(self):
        return reverse('index')
