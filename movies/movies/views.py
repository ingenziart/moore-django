from django.shortcuts import render

data = {
    "movies": [
        {"id": 5, "title": "jaws", "year": 2013},
        {"id": 6, "title": "tom and jerry", "year": 2003},
        {"id": 1, "title": "mr bean", "year": 2008},
    ]
}


def movie(request):
    return render(request, "movies/movies.html", data)
