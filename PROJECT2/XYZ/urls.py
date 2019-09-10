from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
   path('gallery/',views.gall),
]