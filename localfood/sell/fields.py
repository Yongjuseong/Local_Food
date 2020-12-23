import os
from PIL import Image
from django.db.models.fields.files import ImageField,ImageFieldFile

class ThumbnailImageFieldFile(ImageFieldFile): # Define custom ImageFieldFile to write image file and delete it in file system
    def _add_thumb(self,s):
        parts = s.split('.')
        parts.insert(-1,'thumb')
        if parts[-1].lower() not in ('jpeg','jpg'): #Check file extension
            parts[-1]='jpg'
        return '.'.join(parts)

    @property # Define thumb_path property to use method as a member variable.
    def _thumb_path(self):
        return self._add_thumb(self.path)

    @property # Define thumb_url (Thumbnail url)
    def thumb_url(self):
        return self._add_thumb(self.url)

    def save(self,name,content,save=True): # Save Image
        super().save(name,content,save)

        img=Image.open(self.path)
        size=(self.field.thumb_width,self.field.thumb_height)
        img.thumbnail(size)
        background = Image.new('RGB',size,(255,255,255))
        box = (int((size[0] - img.size[0]) / 2), int((size[1] - img.size[1]) / 2))
        background.paste(img,box)
        background.save(self._thumb_path,'JPEG')

    def delete(self, save=True): # Delete Image
        if os.path.exists(self._thumb_path):
            os.remove(self.thumb_url)
        super().delete(save)


class ThumbnailImageField(ImageField): # Define custom ImageField
    attr_class=ThumbnailImageFieldFile

    def __init__(self,verbose_name=None,thumb_width=256,thumb_height=256,**kwargs):
        self.thumb_width,self.thumb_height=thumb_width,thumb_height
        super().__init__(verbose_name,**kwargs)
