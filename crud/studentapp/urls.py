from django.urls import path, include

from crud import views

urlpatterns = [
    path('',views.home, name = '_home'),
    path('add', views.add, name='_add'),
    path('sub', views.sub, name='_sub'),
    path('multiplication/', views.multiplication, name='_multiplication'),
    path('division/', views.division, name='_division'),
]