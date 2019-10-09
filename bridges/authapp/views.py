from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.detail import DetailView

from .models import Users


# Create your views here.

class UserLoginView(LoginView):
    template_name = 'authapp/login.html'


# class UserProfileView(DetailView):
#     pass


class UserLogoutView(LogoutView):
    template_name = 'authapp/logout.html'
