from django.shortcuts import render
from sell.models import Merchandise
from django.views.generic import ListView,DetailView
from django.views.generic import FormView  # Add for search function
from sell.forms import SellSearchForm  # Add for search function
from django.db.models import Q  # Add for search function
from django.shortcuts import render  # Add for search function

#Add these things for add,edit function below.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from localfood.views import OwnerOnlyMixin
from django.views.generic import CreateView,UpdateView,DeleteView

#Add for comment function
from django.conf import settings

# Create your views here.
class SellLV(ListView):
    model=Merchandise

# Edit class for comment function
class SellDV(DetailView):
    model=Merchandise

    # Add a method for comment function
    def get_context_data(self, **kwargs): # For adding context variable
        context = super().get_context_data(**kwargs) # Allocate context variables from original context variables coming from super() method
        context['disqus_short'] = f"{settings.DISQUS_SHORTNAME}" # Get a value of context variables from settings.py
        context['disqus_id'] = f"merchandise-{self.object.id}-{self.object.slug}" # Get a value of context variables from settings.py = ex) merchandise-PK-SLUG
        context['disqus-url'] = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
        context['disqus_title'] = f"{self.object.slug}" # Define the name of page
        return context



#FormView -> if data is vaild , FormView class would do form_valid() function and redirect valid url.
class SearchFormView(FormView): # Define global searchForm
    form_class = SellSearchForm
    template_name = 'sell/global_search.html'

    def form_valid(self,form): # if data(that is from POST request) is valid ->True
        searchWord=form.cleaned_data['search_word'] # if data is valid, input data is in cleaned_data dictionary.
        sell_list=Merchandise.objects.filter(Q(title__icontains=searchWord)| Q(brand__icontains=searchWord)| Q(description__icontains=searchWord)).distinct() # icontains-> i ->Case sensitive X, distinct()->No duplicates

        context={} # Define context as dictionary form
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = sell_list

        return render(self.request,self.template_name,context) # No Redirection, return HttpResponse object

# Add class views for add, edit function below.
class MerchandiseCV(LoginRequiredMixin,CreateView): # Define Merchandise CreateView for every user in LOFOO
    model = Merchandise
    fields = ('title','brand','price','image','description')
    success_url = reverse_lazy('sell:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class MerchandiseChangeLV(LoginRequiredMixin,ListView):  # Define Merchandise ChangeView for every user in LOFOO
    model = Merchandise
    template_name = 'sell/merchandise_change_list.html'

    def get_queryset(self):
        return Merchandise.objects.filter(owner=self.request.user)

class MerchandiseUV(OwnerOnlyMixin,UpdateView): # Define Merchandise UpdateView for the merchandise's owner
    model = Merchandise
    fields = ('title','brand','price','image','description')
    success_url = reverse_lazy('sell:index')

class MerchandiseDelV(OwnerOnlyMixin,DeleteView): # Define Merchandise DeleteView for the merchandise's owner
    model= Merchandise
    success_url = reverse_lazy('sell:index')

