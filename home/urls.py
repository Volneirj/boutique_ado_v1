from django.urls import path
from . import views
from .views import test_upload

urlpatterns = [
    path('', views.index, name='home'),
]