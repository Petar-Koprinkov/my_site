from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog_page, name='blog_page'),
    path('blog/<slug:slug>/', views.blog_detail_page, name='blog_detail_page'),
]