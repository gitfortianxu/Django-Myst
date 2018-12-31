#! /usr/bin/env python
#_*_ coding:utf-8 _*_

"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url,include
from blog import views
from django.conf import settings

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # # url(r'^blog/', include('blog.urls',namespace='blog',app_name='blog')),
    # url(r'^blog/$', views.blog_title,name='blog_title'),
    url(r'^$', views.blog_title,name='blog_title'),
    # url(r'^blog/$', views.blog_title),
    url(r'(?P<article_id>\d)/$', views.blog_article, name='blog_detail'),
]
