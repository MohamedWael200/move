from . import views
from django.urls import path

urlpatterns = [
      path('about' , views.about , name='about'),
      path('home' , views.home , name='home'),
      path('add' , views.add , name='add'),
]