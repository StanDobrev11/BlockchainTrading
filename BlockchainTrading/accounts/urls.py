from django.urls import path

from BlockchainTrading.accounts.views import LoginUserView, RegisterUserView, LogoutUserView, ProfileUserView, \
    PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='login'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('logout/', LogoutUserView.as_view(), name='logout'),

    path('profile/', ProfileUserView.as_view(), name='profile'),
    path('profile/password-change/', PasswordChangeView.as_view(), name='password_change'),
    path('profile/password-change/done/', PasswordChangeDoneView.as_view(), name='password_change_done')
]
