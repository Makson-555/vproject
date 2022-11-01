from django.urls import path, include
from . import views


app_name = 'vpr'
urlpatterns = [
    path('', views.index, name = 'index')
]