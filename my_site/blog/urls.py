from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('blog/', views.BlogPageView.as_view(), name='blog_page'),
    path('blog/<slug:slug>/', views.BlogDetailPageView.as_view(), name='blog_detail_page'),
    path('read-later/', views.ReadLaterView.as_view(), name='read_later'),
]