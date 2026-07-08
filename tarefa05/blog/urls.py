from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:id>/', views.post, name='post'),
]