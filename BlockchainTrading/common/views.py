from django.contrib.auth.decorators import login_required
from django.contrib.auth import mixins as auth_mixins
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView


# Create your views here.
class IndexView(TemplateView):
    template_name = 'common/index.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('dashboard'))
        return super().get(request, args, kwargs)


class DashboardView(auth_mixins.LoginRequiredMixin, TemplateView):
    template_name = 'common/dashboard.html'

#
# @login_required
# # if not logged in wil be redirected to accounts/login
# # if this is not reachable or the url is not that,
# # in settings.py -> :LOGIN_URL = reverse_lazy('login')
#
# def about(request):
#     return HttpResponse(f"About that {request.user}")
