from django.shortcuts import render
from sell.models import Merchandise
from django.views.generic import ListView,DetailView

# Create your views here.
class SellLV(ListView):
    model=Merchandise

class SellDV(DetailView):
    model=Merchandise