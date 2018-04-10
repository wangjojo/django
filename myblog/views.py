#!/usr/bin/env python3
from django.shortcuts import render,redirect
from .models import *
from .forms import CommentForm
from django.http import Http404,HttpResponseRedirect
import json
from users.models import User
# Create your views here.

def index(request):
    return render(request,'blog_index.html')

def get_blogs(request):
    blogs = BlogPost.objects.all().order_by('-pub')
    return render(request,'blog_list.html',{'blogs':blogs })

def get_details(request,blog_id):
    try:
        blog = BlogPost.objects.get(id = blog_id)
    except BlogPost.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)

    ctx = {
        'blog':blog,
        'comments':blog.comment_set.all().order_by('-pub'),
        'form': form 
    }
    
    return render(request,'blog_details.html',ctx)

def accounts_profile(request):
    if request.method == 'POST':
        a = json.loads(request.body.decode('utf-8'))
        print(a)
        b = User.objects.get(email = request.user.email)
        b.name = a['name']
        b.sex = a['sex']
        b.job = a['job']
        b.phone = a['phone']

        b.save()

    return render(request,'accounts_profile.html')