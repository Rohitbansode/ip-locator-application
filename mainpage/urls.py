from django.urls import path
from . import views

urlpatterns = [
    path('', views.ip_locator, name='ip_locator'),
]
