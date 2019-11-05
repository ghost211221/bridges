# -*- coding: utf-8 -*-

from django.shortcuts import render

from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from django.contrib.auth.mixins import  PermissionRequiredMixin

from django.db.models import Q

from .models import News
from .models import TechnicalSolutions
from .models import NewsHasTechnicalSolutions
from .models import NewsDiscussItem


# Create your views here.
class NewsListView(ListView):
    """docstring for ProductList"""    
    model = News

    template_name = 'newsapp/blog.html'
    extra_context = {}

    def get_queryset(self):
        return News.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = TechnicalSolutions.objects.all()
        news_category = NewsHasTechnicalSolutions.objects.all()
        latest_news = context['object_list'][:3]

        comments = NewsDiscussItem.objects.all()
        for news in context['object_list']:
            catList = []
            commentsList = []
            for category in news_category:
                if news.id == category.news:
                    catList.append(category.news_id)
            for comment in comments:
                if news.id == comment.news_id:
                    commentsList.append(comment.comment)
            setattr(news, 'catList', catList)
            setattr(news, 'comments', commentsList)
            setattr(news, 'commentsLen', len(commentsList))
        context.update({'products': products,
                        'news_category': news_category,
                        'latest_news': latest_news,
        })
        return context

# Create your views here.
class NewsDetailView(DetailView):
    """docstring for ProductList"""    
    model = News

    products = TechnicalSolutions.objects.all()
    latest_news = News.objects.all()[:3]
    comments = NewsDiscussItem.objects.all()

    template_name = 'newsapp/blog_detail.html'
    extra_context = {}
    extra_context.update({'products': products,
                        'latest_news': latest_news,
    })

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs['object'].id
        news_category = NewsHasTechnicalSolutions.objects.filter(news_id=pk)
        comments = NewsDiscussItem.objects.filter(news_id=pk)
        # commentators = NewsDiscussItem.objects.filter(news_id=pk)
        context.update({
            'news_category': news_category,
            'comments': comments,
            'commentsLen': len(comments),
        })
        return context


# Create your views here.
class NewsCreateView(PermissionRequiredMixin, CreateView):
    """docstring for ProductList"""    
    model = News

    template_name = 'newsapp/blog.html'
    extra_context = {}


# Create your views here.
class NewsUpdateView(PermissionRequiredMixin, UpdateView):
    """docstring for ProductList"""    
    model = News

    template_name = 'newsapp/blog.html'
    extra_context = {}




# Create your views here.
class NewsDeleteView(PermissionRequiredMixin, DeleteView):
    """docstring for ProductList"""    
    model = News

    template_name = 'newsapp/blog.html'
    extra_context = {}


