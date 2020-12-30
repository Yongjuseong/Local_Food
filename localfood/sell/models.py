from django.db import models
from django.urls import reverse
from sell.fields import ThumbnailImageFieldFile
from sell.fields import ThumbnailImageField # Define custom field

# Create your models here.
class Merchandise(models.Model): # Define Merchandise table
    title=models.CharField('TITLE',max_length=30)
    brand=models.CharField('BRAND',max_length=30)
    slug = models.SlugField('SLUG',unique=True, allow_unicode=True, help_text='one word for title alias')
    price = models.FloatField('PRICE')
    image=ThumbnailImageField(upload_to='merchandise/%Y/%m')
    description = models.TextField('Merchandise Description',blank=True)
    rating = models.FloatField('RATING')
    create_dt = models.DateTimeField('CREATE DATE',auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE',auto_now=True)
    #owner = models.ForeignKey('auth.User',on_delete=models.CASCADE,verbose_name='OWNER',blank =True,null=True) # Add for editting contents

    class Meta:
        ordering=('id',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('sell:sell_detail',args=(self.id,))
