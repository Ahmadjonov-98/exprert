from django.urls import path
from .views import Home, About,Help,Blog

urlpatterns = [
	path('',Home.as_view(),name='home'),
	path('about/',About.as_view(),name='about'),
	path('help/',Help.as_view(),name='help'),
	path('blog/',Blog.as_view(),name='blog'),
]
