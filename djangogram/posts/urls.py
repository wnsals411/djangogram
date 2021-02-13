from django.urls import path
from djangogram.posts import views

app_name = "posts"
urlpatterns = [
    path('', views.index, name='index'),
]
