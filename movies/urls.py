from django.urls import path
from movies import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home),
    path('movies', views.movies, name='movies'),
    path('movies/<int:id>', views.movieDetails, name='moviedetails'),
    path('movies/<str:movieCategory>', views.category, name='category'),
    path('favorite', views.favorite, name='favorite'),
    path('favorite/add/<int:id>', views.addFavorite, name='addFavorite'),
    path('favorite/remove/<int:id>', views.removeFavorite, name="removeFavorite")

]
