from django.contrib.auth.views import LoginView
from django.urls import path

from BlockchainTrading.common.views import IndexView, DashboardView

urlpatterns = [

    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('', IndexView.as_view(), name='index'),
    # path('about/', about, name='about')
]
