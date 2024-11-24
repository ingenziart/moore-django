from django.shortcuts import render
from .models import Movie

data = Movie.objects.all()


def movie(request):
    return render(request, "movies/movies.html", {"movies": data})


def details(request, id):
    data = Movie.objects.get(pk=id)
    return render(request, "movies/details.html", {"movie": data})
