from django.contrib import admin
from django.urls import path
from sell import views

app_name = 'sell'

urlpatterns = [
    #Example: /sell/
    path('',views.SellLV.as_view(),name='index'),

    #Example: /sell/sell/99
    path('sell/<int:pk>/',views.SellDV.as_view(),name='sell_detail'),

    #Example: /sell/search/
    path('search/',views.SearchFormView.as_view(),name='global_search'),
]
