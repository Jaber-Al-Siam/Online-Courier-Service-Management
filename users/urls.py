from typing import Any, List
from django.urls import path
from users import views as users_views
from django.contrib.auth import views as auth_views

urlpatterns: List[Any] = [
    path('', users_views.home, name='home_page'),
    path('signup/', users_views.UserCreationView.as_view(), name='signup_page'),
    path('profile/', users_views.viewOrUpdateProfile, name='profile_page'),
    path('login/', auth_views.LoginView.as_view(), name='login_page'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout_page'),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset_page'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done_page'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm_page'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete_page'),
]
