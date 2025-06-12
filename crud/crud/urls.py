from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name = '_home'),
    path('add', views.add, name='_add'),
    path('sub', views.sub, name='_sub'),
    path('multiplication/', views.multiplication, name='_multiplication'),
    path('division/', views.division, name='_division'),
]