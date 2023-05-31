from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('new_post/', views.creating),
    path('check_posts', views.check_posts)
    ]