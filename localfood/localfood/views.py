from django.views.generic import TemplateView

#Add for 3 auth functions below.
from django.views.generic import CreateView # generic view -> for dealing with changing data in table
from django.contrib.auth.forms import  UserCreationForm
from django.urls import reverse_lazy # reverse() X-> urls.py module can't be loaded before doing and loading views.py module


class HomeView(TemplateView): #Define Home View
    template_name = 'home.html'


class UserCreateView(CreateView): # Define User Create View
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView): # Define User Create Done View
    template_name = 'registration/register_done.html'