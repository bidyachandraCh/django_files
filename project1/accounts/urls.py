from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path
from . import views
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('',views.home),
    path('login/', LoginView.as_view(template_name='htmlfiles/login.html'), name="login"),
]