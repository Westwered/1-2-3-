from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.views.generic import TemplateView
from .views import register
from .views import order_certificate, order_success

def logout_view(request):
    logout(request)
    return redirect('login')

urlpatterns = [
    path('', TemplateView.as_view(template_name='core/index.html'), name='home'),
    path('register/', register, name='register'),
    path('order/', order_certificate, name='order_certificate'),
    path('order/success/', order_success, name='order_success'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
]