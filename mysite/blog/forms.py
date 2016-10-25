# -*- conding: utf-8 -*-
'''
Created on 2016. 10. 24.

@author: swhong
'''
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')