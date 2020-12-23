from django.contrib import admin
from sell.models import Merchandise

# Register your models here.

@admin.register(Merchandise) #Using decorater than admin.site.register() function to be simple
class MerchandiseAdmin(admin.ModelAdmin):
    list_display = ('id','title','brand','price','modify_dt')
    list_filter=('brand','modify_dt')
    search_fields=('title','brand','owner')
    prepopulated_fields = {'slug': ('title',)}