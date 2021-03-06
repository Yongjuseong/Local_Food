"""localfood URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import  static # Add for sell.image
from django.conf import settings # Add for sell.image
from localfood.views import HomeView # Add HomeView
from localfood.views import UserCreateView, UserCreateDoneTV # Add for auth function  # 인증 기능을 위해 추가

urlpatterns = [
    path('admin/', admin.site.urls),
    # Add 3 urls for auth functions below / 인증 기능을 위해 아래 3개 url 정의, 추가
    path('accounts/', include('django.contrib.auth.urls')),  # Basic django's URLconf(/login/,logout/)
    path('accounts/register/',UserCreateView.as_view(),name='register'), # Define create account url
    path('accounts/register/done/',UserCreateDoneTV.as_view(),name='register_done'), # Define done url after creating account url
    #-----
    path('',HomeView.as_view(),name='home'), # Add Home view
    path('sell/', include('sell.urls')), # Add sell app's url
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT) # Add for sell.image
