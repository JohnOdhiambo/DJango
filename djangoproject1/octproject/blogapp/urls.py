
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog,name='blog'),
    path('blog_details.html',views.blog_details,name='blog_details'),
    path('post/<slug:url>', views.post_detail,name='postdetail'),
    path('search',views.search,name='search'),
    path('about.html',views.about,name='about'),
    path('services.html',views.services,name='services'),
    path('contact.html',views.contact,name='contact')
]


