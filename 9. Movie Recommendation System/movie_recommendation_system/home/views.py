from django.shortcuts import render
from home.ml.ml_utils import get_all_movies, recommend

# Create your views here.
def home(request):
    movies = get_all_movies()
    if request.method == 'POST':
        selected_movie = request.POST.get('selected_movie')
        rec_movie = recommend(selected_movie)
        data = {
            "movies":movies,
            "rec_movie":rec_movie
        }
        return render(request, 'home.html', data)
    return render(request, 'home.html', {'movies':movies})