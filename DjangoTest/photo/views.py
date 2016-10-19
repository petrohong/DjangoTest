# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from .models import Photo
from django.shortcuts import get_object_or_404, render, redirect
from photo.forms import PhotoEditForm
# Create your views here.
'''
def single_photo(request, *args):
    return HttpResponse('{0}번...{0}번 사진을 보여드릴께요'.format(args[0]))
'''
#사진이 없을 경우 exception 처리를 해야함
def single_photo(request, photo_id):
#     try:
#         photo = Photo.objects.get(pk=photo_id)
#     except Photo.DoesNotExist:
#         return HttpResponse("사진이 없습니다!!!!")
    photo = get_object_or_404(Photo, pk=photo_id) #위 구문을 하나로.. 없는 경우 404로 바로 전달.
#     response_text = '<p>{photo_id} 번...{photo_id}번 사진을 보여드릴께요.</p>'
#     response_text += '<p>{photo_url}</p>'
#     response_text += '<p><img src="{photo_url}" /></p>'

    return render(request, 
                  'photo_view.html', 
                  {
                      'photo': photo,
                      }
                  )
    
def new_photo(request):
    if request.method == "GET":
        edit_form = PhotoEditForm()
    elif request.method == "POST":
        edit_form = PhotoEditForm(request.POST, request.FILES)
        if edit_form.is_valid() :
            new_photo = edit_form.save()
            return redirect(new_photo.get_absolute_url())
        
    return render(request,
        'new_photo.html',
         {
            'form' : edit_form,
         }
     )