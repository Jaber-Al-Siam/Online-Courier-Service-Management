from typing import Any, List
from django.urls import path
from users import views as users_views
from django.contrib.auth import views as auth_views

urlpatterns: List[Any] = [
    path('', users_views.home, name='home_page'),
    path('signup/', users_views.signup, name='signup_page'),
    path('profile/', users_views.viewOrUpdateProfile, name='profile_page'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login_page'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logged_out.html'), name='logout_page'),
    path('password-reset/', auth_views.PasswordResetView.as_view(
        template_name='users/password_reset.html'), name='password_reset_page'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='password_reset_done.html'), name='password_reset_done_page'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='password_reset_confirm.html'), name='password_reset_confirm_page'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='password_reset_complete.html'), name='password_reset_complete_page'),
]
