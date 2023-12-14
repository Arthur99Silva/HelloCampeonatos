from django.contrib import admin
from django.urls import path
from tasks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('sair/', views.sair, name='sair'),
    path('userpage/', views.userpage, name='userpage'),
    path('admin/', views.admin, name='admin'),
    path('profile/', views.profile, name='profile'),
    path('editprofile/', views.editprofile, name='editprofile'),
    # Histórico
    path('historico/', views.historico, name='historico'),
    #Equipe
    path('equipe/', views.equipe, name='equipe'),
    path('equipe/list/', views.equipe_list, name='equipe_list'),
    path('equipe/editar/<int:equipe_id>/', views.editar_equipe, name='editar_equipe'),
    path('equipe/excluir/<int:equipe_id>/', views.excluir_equipe, name='excluir_equipe'),
    path('editar_equipe/<int:equipe_id>/', views.editar_equipe, name='editar_equipe'),
    #Estádios
    path('estadio/', views.estadio, name='estadio'),
    path('estadio/list/', views.estadio_list, name='estadio_list'),
    path('estadio/editar/<int:estadio_id>/', views.editar_estadio, name='editar_estadio'),
    path('estadio/excluir/<int:estadio_id>/', views.excluir_estadio, name='excluir_estadio'),
    path('editar_estadio/<int:estadio_id>/', views.editar_estadio, name='editar_estadio'),
    #Técnicos
    path('tecnico/', views.tecnico, name='tecnico'),
    path('tecnico/list/', views.tecnico_list, name='tecnico_list'),
    path('tecnico/editar/<int:tecnico_id>/', views.editar_tecnico, name='editar_tecnico'),
    path('tecnico/excluir/<int:tecnico_id>/', views.excluir_tecnico, name='excluir_tecnico'),
    path('editar_tecnico/<int:tecnico_id>/', views.editar_tecnico, name='editar_tecnico'),
    #Campeonato
    path('campeonato/', views.campeonato, name='campeonato'),
    path('campeonato-list/', views.campeonato_list, name='campeonato_list'),
    path('campeonato/editar/<int:campeonato_id>/', views.editar_campeonato, name='editar_campeonato'),
    path('campeonato/excluir/<int:campeonato_id>/', views.excluir_campeonato, name='excluir_campeonato'),
    path('editar_campeonato/<int:campeonato_id>/', views.editar_campeonato, name='editar_campeonato'),
    #Jogador
    path('jogador/', views.jogador, name='jogador'),
    path('jogador/list/', views.jogador_list, name='jogador_list'),
    path('jogador/editar/<int:jogador_id>/', views.editar_jogador, name='editar_jogador'),
    path('jogador/excluir/<int:jogador_id>/', views.excluir_jogador, name='excluir_jogador'),
    path('editar_jogador/<int:jogador_id>/', views.editar_jogador, name='editar_jogador'),
    #Desempenho
    path('desempenho/', views.desempenho, name='desempenho'),
    path('desempenho/list/', views.desempenho_list, name='desempenho_list'),
    path('desempenho/editar/<int:desempenho_id>/', views.editar_desempenho, name='editar_desempenho'),
    path('desempenho/excluir/<int:desempenho_id>/', views.excluir_desempenho, name='excluir_desempenho'),
    path('editar_desempenho/<int:desempenho_id>/', views.editar_desempenho, name='editar_desempenho'),
    #Partida
    path('partida/', views.partida, name='partida'),
    path('partida/list/', views.partida_list, name='partida_list'),
    path('partida/editar/<int:partida_id>/', views.editar_partida, name='editar_partida'),
    path('partida/excluir/<int:partida_id>/', views.excluir_partida, name='excluir_partida'),
    path('editar_partida/<int:partida_id>/', views.editar_partida, name='editar_partida'),
    #Escalacao
    path('escalacao/', views.escalacao, name='escalacao'),
    path('escalacao-list/', views.escalacao_list, name='escalacao_list'),
    path('escalacao/editar/<int:escalacao_id>/', views.editar_escalacao, name='editar_escalacao'),
    path('escalacao/excluir/<int:escalacao_id>/', views.excluir_escalacao, name='excluir_escalacao'),
    path('editar_escalacao/<int:escalacao_id>/', views.editar_escalacao, name='editar_escalacao'),
    #Substituicao
    path('substituicao/', views.substituicao, name='substituicao'),
    path('substituicao/', views.substituicao_list, name='substituicao_list'),
    path('substituicao/editar/<int:substituicao_id>/', views.editar_substituicao, name='editar_substituicao'),
    path('substituicao/excluir/<int:substituicao_id>/', views.excluir_substituicao, name='excluir_substituicao'),
    path('editar_substituicao/<int:substituicao_id>/', views.editar_substituicao, name='editar_substituicao'),
  ]
