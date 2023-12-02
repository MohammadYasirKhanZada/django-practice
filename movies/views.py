from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from .models import Movie

# Create your views here.
def movies(request):
    data = Movie.objects.all()
    return render(request, "movies/movies.html", {'movies': data})

# HOME ROUTE
def home(request):
    return HttpResponse("Home page.")

# MOVIES DETAIL ROUTE
def detail(request, id):
    data = Movie.objects.get(pk=id)
    return render(request, 'movies/detail.html', {'movie': data})

# ADD ROUTE
def add(request):
    title = request.POST.get("title")
    year = request.POST.get("year")

    if title and year:
        movie = Movie(title=title, year=year)
        movie.save()
        return HttpResponseRedirect("/movies")
    
    return render(request, "movies/add.html")

# DELETE ROUTE.
def delete(request, id):
    try:
        movie = Movie.objects.get(pk=id)
    except:
        raise Http404("Movie Does not exits.")
    movie.delete()
    return HttpResponseRedirect('/movies')