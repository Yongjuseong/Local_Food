from django import forms

class SellSearchForm(forms.Form): #Define SearchForm by inheriting form class from django.forms
    search_word = forms.CharField(label='Search Word') # label => "Search Word" that is printed in front of form widget / it means <input type ="text"> in HTML.