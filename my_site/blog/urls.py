from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('blog-page/', views.BlogPageView.as_view(), name='blog_page'),
    path('blog-detail-page/<slug:slug>/', views.BlogDetailPageView.as_view(), name='blog_detail_page'),
    path('read-later/', views.ReadLaterView.as_view(), name='read_later'),
]