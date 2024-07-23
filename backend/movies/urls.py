from django.urls import path
from movies import views

urlpatterns = [

    # Public pages

    path('', views.releases, name='releases'),
    path('index/', views.releases, name='releases'),
    path('types/<str:type>/', views.types, name='types'),
    path('searchs/', views.searchs, name='searchs'),
    path('movie/<int:id>/', views.movie_select, name='movie_select'),

]