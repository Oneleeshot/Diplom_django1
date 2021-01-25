from django.urls import path
from django.contrib.auth import views
from .views import register_user

app_name = 'account'

urlpatterns = [
    path('login/',
         views.LoginView.as_view(template_name='registration/login.html'),
         name='login'),
    path('logged_out/',
         views.LogoutView.as_view(
             template_name='registration/logged_out.html'),
         name='logged_out'),
    path('register/', register_user, name='register'),

]
