from django.contrib.auth import forms as auth_forms, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import views as auth_views, get_user_model
from django.urls import reverse, reverse_lazy
from django.views import generic as views
from django.contrib.auth import mixins as auth_mixins

from BlockchainTrading.accounts.forms import UserCreateForm

# Create your views here.

# authenticate(request, **credentials) -> returns the user if credentials match
# login(request, user) -> attaches a cookie for the authenticated user

# correct way of importing user is:
UserModel = get_user_model()


# in the settings.py, add configuration AUTH_USER_MODEL = 'accounts/AppUSer'

class LoginUserView(auth_views.LoginView):
    template_name = 'account/login_user.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('dashboard'))
        return super().get(request, args, kwargs)

    # def get_success_url(self):
    #     return reverse_lazy('dashboard')

    # if next is not provided, it should redirect to dashboard, tfore in settings.py =>
    # LOGIN_REDIRECT_URL = reverse_lazy('dashboard)


class RegisterUserView(views.CreateView):
    # form_class = auth_forms.UserCreationForm  # default form in Django for user creation
    form_class = UserCreateForm  # default form in Django for user creation
    template_name = 'account/register_user.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        valid = super().form_valid(form)
        login(self.request, self.object)
        return valid


class LogoutUserView(auth_views.LogoutView):

    def get_success_url(self):
        return reverse('index')


class ProfileUserView(views.TemplateView, auth_mixins.LoginRequiredMixin):
    template_name = 'account/profile.html'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     user = self.request.user
    #     context['user'] = user
    #
    #     return context


class PasswordChangeView(auth_views.PasswordChangeView, auth_mixins.LoginRequiredMixin):
    template_name = 'account/password_change.html'


class PasswordChangeDoneView(auth_views.PasswordChangeDoneView, auth_mixins.LoginRequiredMixin):
    template_name = 'account/password_change_done.html'
