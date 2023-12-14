from django.contrib import admin

# Register your models here.
from .models import Equipe, Jogador, Estadio, Substituicao, Tecnico, Escalacao, Campeonato, Partida, Desempenho

admin.site.register(Equipe)
admin.site.register(Jogador)
admin.site.register(Substituicao)
admin.site.register(Tecnico)
admin.site.register(Escalacao)
admin.site.register(Campeonato)
admin.site.register(Partida)
admin.site.register(Desempenho)
admin.site.register(Estadio)