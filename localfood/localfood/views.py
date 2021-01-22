from django.views.generic import TemplateView

#Add for 3 auth functions below.
from django.views.generic import CreateView # generic view -> for dealing with changing data in table
from django.contrib.auth.forms import  UserCreationForm
from django.urls import reverse_lazy # reverse() X-> urls.py module can't be loaded before doing and loading views.py module

#Add for add, edit function
from django.contrib.auth.mixins import AccessMixin # Distinguish proper permission or not , when processing handling view phase

class HomeView(TemplateView): #Define Home View
    template_name = 'home.html'


class UserCreateView(CreateView): # Define User Create View
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register_done')

class UserCreateDoneTV(TemplateView): # Define User Create Done View
    template_name = 'registration/register_done.html'


# Add Mixin class for add, edit function
class OwnerOnlyMixin(AccessMixin): # Whether distinguish that the user has permission of this content or not
    raise_exception = True # 403 Exception
    permission_denied_message = "Owner only can update/delete the object" # 403 Exception message

    def dispatch(self,request, *args,**kwargs): # Overriding dispatch() method, to distinguish owner before get() method
        obj = self.get_object() # Get obejct from table
        if request.user != obj.owner:
            return self.handle_no_permission()
        return super().dispatch(request,*args,**kwargs)