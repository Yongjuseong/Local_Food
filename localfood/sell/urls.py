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

    #Example: /sell/merchandise/add/
    path('merchandise/add/',views.MerchandiseCV.as_view(),name='merchandise_add'),

    #Example: /sell/merchandise/change
    path('merchandise/change/',views.MerchandiseChangeLV.as_view(),name='merchandise_change'),

    #Example: /sell/merchandise/update
    path('merchandise/<int:pk>/update/',views.MerchandiseUV.as_view(),name='merchandise_update'),

    #Example: /sell/merchandise/delete
    path('merchandise/<int:pk>/delete/',views.MerchandiseDelV.as_view(),name='merchandise_delete'),
]
