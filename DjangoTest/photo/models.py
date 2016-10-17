# -*- coding:utf-8 -*-

from django.db import models

# Create your models here.
class Photo(models.Model):
    id = models.AutoField(primary_key=True)
    image_file = models.ImageField(upload_to='static_files/uploaded/original/%Y%m%d')
    filtered_image_file = models.ImageField(upload_to='static_files/uploaded/filtered/%Y%m%d')
    description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def delete(self, *args, **kwargs):
        self.image_file.delete()
        self.filtered_image_file.delete()
        super(Photo, self).delete(*args, **kwargs)