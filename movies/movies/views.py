from django.shortcuts import render
from .models import Movie

data = Movie.objects.all()


def movie(request):
    return render(request, "movies/movies.html", {"movies": data})
