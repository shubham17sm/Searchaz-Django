from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('search/<query>/<int:num>/', views.search, name='search'),
]