from typing import Any, List
from django.urls import path
from users import views as users_views
from django.contrib.auth import views

urlpatterns: List[Any] = [
    # path('signup/', '#', name='signup_page'),
    path('', users_views.home, name='home_page'),
    path('login/', views.LoginView.as_view(template_name='login.html'), name='login_page'),
]
