from django.shortcuts import render
from .models import Movie
from django.http import HttpResponseRedirect

data = Movie.objects.all()


def movie(request):
    return render(request, "movies/movies.html", {"movies": data})


def details(request, id):
    data = Movie.objects.get(pk=id)
    return render(request, "movies/details.html", {"movie": data})


def add(request):
    title = request.POST.get("title")
    year = request.POST.get("year")

    if title and year:
        movie = Movie(title=title, year=year)
        movie.save()
        return HttpResponseRedirect("/movies")

    return render(request, "movies/add.html")


def famos(request):
    title = request.POST.get("title")
    year = request.POST.get("year")
    if title and year:
        movie = Movie(title=title, year=year)
        movie.save()
        HttpResponseRedirect("/movies")

    return render(request, "movies/famos.html")
