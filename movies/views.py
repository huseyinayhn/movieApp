from django.shortcuts import render
from .models import Category, Movie
from django.http import HttpResponseRedirect


# Create your views here.
def home(req):
    data = {
        'categories': Category.objects.all(),
        'movies': Movie.objects.filter(in_main_page=True),
    }
    return render(req, 'index.html', data)


def movies(req):
    data = {
        'categories': Category.objects.all(),
        'movies': Movie.objects.all(),
    }
    return render(req, 'movies.html', data)


def movieDetails(req, id):
    data = {
        'movie': Movie.objects.get(id=id)
    }
    return render(req, 'details.html', data)



def category(req, movieCategory):
    data = {
        'categories': Category.objects.all(),
        'movies': Movie.objects.all(),
        'moviecategory': movieCategory,
    }
    return render(req, 'category.html', data)


fav = []


def favorite(req):
    data = {
        'movies': Movie.objects.filter(id__in=fav),
    }

    return render(req, 'favorites.html', data)


def addFavorite(req, id):
    isFind = False
    for x in fav:
        if id == x:
            isFind = True
            break

    print(isFind)
    if isFind == True:
        return HttpResponseRedirect('/home')
    else:
        fav.append(id)
        return HttpResponseRedirect('/favorite')

def removeFavorite(req, id):
    for key in fav:
        if key == id:
            fav.remove(key)

    return HttpResponseRedirect('/favorite')