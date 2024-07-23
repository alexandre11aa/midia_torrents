from django.db import models

KEYWORD_CHOICES = [
    ('acao', 'Ação'),
    ('animacao', 'Animação'),
    ('aventura', 'Aventura'),
    ('biografia', 'Biografia'),
    ('comedia', 'Comédia'),
    ('crime', 'Crime'),
    ('documentario', 'Documentário'),
    ('drama', 'Drama'),
    ('fantasia', 'Fantasia'),
    ('ficcao', 'Ficção'),
    ('familia', 'Família'),
    ('guerra', 'Guerra'),
    ('historia', 'História'),
    ('misterio', 'Mistério'),
    ('musical', 'Musical'),
    ('policial', 'Policial'),
    ('romance', 'Romance'),
    ('suspense', 'Suspense'),
    ('terror', 'Terror'),
    ('esporte', 'Esporte'),
]

MEDIA_TYPE = [
    ('series', 'Séries'),
    ('filmes', 'Filmes'),
]

class movie(models.Model):

    id = models.AutoField(primary_key=True)
    date = models.DateTimeField(auto_now_add=True)
    poster = models.CharField(max_length=150, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    original_name = models.CharField(max_length=50, null=True, blank=True)
    direction = models.CharField(max_length=50, null=True, blank=True)
    release_date = models.DateField(null=True, blank=True)
    duration = models.CharField(max_length=20, null=True, blank=True)
    imdb = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    language = models.CharField(max_length=50, null=True, blank=True)
    quality = models.CharField(max_length=50, null=True, blank=True)
    synopsis = models.TextField(max_length=500, null=True, blank=True)
    year = models.DecimalField(max_digits=4, decimal_places=0, null=True, blank=True)
    keyword_1 = models.CharField(max_length=50, choices=KEYWORD_CHOICES, null=True, blank=True)
    keyword_2 = models.CharField(max_length=50, choices=KEYWORD_CHOICES, null=True, blank=True)
    keyword_3 = models.CharField(max_length=50, choices=KEYWORD_CHOICES, null=True, blank=True)
    keyword_4 = models.CharField(max_length=50, choices=MEDIA_TYPE, null=True, blank=True)
    trailer = models.URLField(null=True, blank=True)
    torrent_720 = models.URLField(null=True, blank=True)
    torrent_1080 = models.URLField(null=True, blank=True)

    def __str__(self):
        return f'{self.id} - {self.name}'