from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new_pr', views.new_pr),
]

