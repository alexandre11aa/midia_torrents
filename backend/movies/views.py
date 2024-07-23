from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import movie
import re

def releases(request):
    last_movies = movie.objects.order_by('-release_date')[:10]

    total_movies = movie.objects.all()

    return render(request, 'index.html', {'last_movies': last_movies,
                                          'total_movies': total_movies})

def types(request, type):
    total_movies = movie.objects.filter(
        Q(keyword_1__iexact=type) |
        Q(keyword_2__iexact=type) |
        Q(keyword_3__iexact=type) |
        Q(keyword_4__iexact=type)
    )

    return render(request, 'types.html', {'total_movies': total_movies,
                                          'type': type.upper()})

def searchs(request):
    
    query = request.GET.get('query', '')

    search_movies = movie.objects.filter(
        Q(name__icontains=query) |
        Q(original_name__icontains=query) |
        Q(synopsis__icontains=query)
    )

    return render(request, 'searchs.html', {'search_movies': search_movies,
                                            'query': query.upper()})

def extract_youtube_id(url):
    match = re.search(r'youtube\.com/watch\?v=([^\&\?\/]+)', url)
    if match:
        return match.group(1)
    return None

def movie_select(request, id):
    movie_selected = get_object_or_404(movie, pk=id)
    
    # Formatar o link para incorporação
    trailer_url = movie_selected.trailer
    youtube_id = extract_youtube_id(trailer_url)
    if youtube_id:
        trailer_embed_url = f"https://www.youtube.com/embed/{youtube_id}"
    else:
        trailer_embed_url = None
    
    context = {
        'details': movie_selected,
        'trailer_embed_url': trailer_embed_url
    }
    
    return render(request, 'movie.html', context)