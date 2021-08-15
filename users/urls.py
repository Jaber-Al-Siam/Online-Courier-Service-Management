from typing import Any, List
from django.urls import path
from users import views as customer_views
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns: List[Any] = [
    path('', customer_views.home, name='home'),
    path('signup/', customer_views.CustomerCreationView.as_view(), name='customer_signup'),
    path('user/<int:pk>/', customer_views.UserDetailView.as_view(), name='user_detail'),
    path('customer/<int:pk>/', customer_views.CustomerDetailView.as_view(), name='customer_detail'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),
]
