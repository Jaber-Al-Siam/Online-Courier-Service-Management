from typing import Any, List
from django.urls import path
from django.contrib.auth import views

urlpatterns: List[Any] = [
    # path('signup/', '', name='signup_page'),
    path('login/', views.LoginView.as_view(template_name='user/login.html'), name='login_page'),
]
