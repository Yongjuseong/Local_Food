from django.shortcuts import render
from sell.models import Merchandise
from django.views.generic import ListView,DetailView
from django.views.generic import FormView  # Add for search function
from sell.forms import SellSearchForm  # Add for search function
from django.db.models import Q  # Add for search function
from django.shortcuts import render  # Add for search function


# Create your views here.
class SellLV(ListView):
    model=Merchandise

class SellDV(DetailView):
    model=Merchandise


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




