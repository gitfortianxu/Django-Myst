#! /usr/bin/env python
#_*_ coding:utf-8 _*_


from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from account.forms import LoginForm
from blog.models import BlogArticles
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request,'blog/titles.html',{'blogs':blogs})

def blog_article(request,article_id):
    # article = BlogArticles.objects.get(id=article_id)
    article = get_object_or_404(BlogArticles,id=article_id)
    pub = article.publish
    return render(request,'blog/content.html',{'article':article,'publish':pub})

def user_login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])

            if user:
                login(request,user)
                return HttpResponse('Welcome you!')
            else:
                return HttpResponse('SORRY YOU ARE NOT USER!')

        else:
            return HttpResponse('Invalid login')

    if request.method == 'GET':
        login_form = LoginForm()
        return render(request,'account/login.html',{'form':login_form})