from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ajax/loading/', views.loading,name='loading'),
]
