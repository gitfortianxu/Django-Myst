#! /usr/bin/env python
#_*_ coding:utf-8 _*_

from django import forms
from .models import ArticleColumn
from .models import ArticlePost
from .models import Comment

class ArticleColumnForm(forms.ModelForm):
    class Meta:
        model =ArticleColumn
        fields = ('column',)

class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = ArticlePost
        fields = ("title", "body")

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('commentator','body',)


