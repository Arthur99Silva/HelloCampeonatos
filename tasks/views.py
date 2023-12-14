from datetime import timedelta
from django.http import HttpResponse
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import UserUpdateForm
from .models import Equipe, Estadio, Tecnico, Campeonato, Jogador, Desempenho, Partida, Escalacao, Substituicao
from .forms import EquipeForm, EstadioForm, TecnicoForm, CampeonatoForm, JogadorForm, DesempenhoForm, PartidaForm, EscalacaoForm, SubstituicaoForm

#Métodos 
def home(request):
    return render(request, 'home.html')

def signup(request):

    if request.method == 'GET':

        return render(request, 'signup.html', {
            'form': UserCreationForm
        })

    else:
        if request.POST['password1'] == request.POST['password2']:

            try:

                user = User.objects.create_user(
                    first_name = request.POST['first_name'], username=request.POST['username'], password=request.POST['password1'])
                user.save()
                # Adicione o usuário ao grupo 'usuario' (ou ao grupo que você desejar)
                grupo_usuario = Group.objects.get(name='costumer')
                user.groups.add(grupo_usuario)
                login(request, user)

                return redirect('userpage')

            except:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'Usuário já existe'

                })

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'senhas são diferentes'

        })

def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Usuário ou senha está incorreto'
            })
        else:
            login(request, user)

            # Verificar o grupo do usuário
            if user.groups.filter(name='costumer').exists():
                return redirect('userpage')
            elif user.groups.filter(name='admin').exists():
                return redirect('admin')
            else:
                # Redirecionar para uma página padrão se não estiver em nenhum grupo específico
                return redirect('home')
            
@login_required
def sair(request):
    logout(request)
    return redirect('home')

@login_required
def admin(request):
    return render(request, 'admin.html')

@login_required
def userpage(request):
    if request.method == 'POST':
        if "profile" in request.POST:
            return redirect('profile')
        if "equipe" in request.POST: 
            return redirect('equipe')
        if "historico" in request.POST:
            return redirect('historico')

    return render(request, 'userpage.html')

@login_required
def profile(request):
    if request.method == 'POST':
        if "update" in request.POST:
            return redirect('editprofile')
        if "delete" in request.POST:
            user_pk = request.user.pk
            logout(request)
            User = get_user_model()
            User.objects.filter(pk=user_pk).delete()
            return redirect('home')
        if "return" in request.POST:
            return redirect('userpage')
    else:
        return render(request, 'profile.html')

@login_required
def editprofile(request):
    if request.method == 'POST':
        if "return" in request.POST:
            return redirect('profile')
        if "confirm" in request.POST:
            if request.POST['password1'] == request.POST['password2']:
                try:
                    user = request.user
                    if request.POST['username'] != '':
                        user.username = request.POST['username']
                    if request.POST['first_name'] != '':
                        user.first_name = request.POST['first_name']
                    if request.POST['password1'] != '':
                        user.set_password(request.POST['password1'])
                    logout(request)
                    user.save()
                    login(request, user)
                    return redirect('profile')

                except:
                    return render(request, 'editprofile.html', {
                        'form': UserUpdateForm,
                        "error": 'Usuário já existe'

                    })

        return render(request, 'editprofile.html', {
            'form': UserUpdateForm,
            "error": 'senhas são diferentes'

        })

    else:
        return render(request, 'editprofile.html', {
            'form': UserUpdateForm
        })
    
@login_required
def equipe(request):
    if request.method == 'POST':
        form = EquipeForm(request.POST)
        if form.is_valid():
            equipe_instance = form.save(commit=False)
            equipe_instance.user = request.user
            equipe_instance.save()
            return redirect('equipe_list')
    else:
        form = EquipeForm()

    return render(request, 'userpage.html', {'form': form})

def equipe_list(request):
    equipe_list = Equipe.objects.all()
    return render(request, 'equipe_list.html', {'equipe_list': equipe_list})

@login_required
def editar_equipe(request, equipe_id):
    equipe = get_object_or_404(Equipe, pk=equipe_id)
    
    if request.method == 'POST':
        form = EquipeForm(request.POST, instance=equipe)
        if form.is_valid():
            form.save()
            return redirect('equipe_list')
    else:
        form = EquipeForm(instance=equipe)

    return render(request, 'editar_equipe.html', {'form': form})

@login_required
def excluir_equipe(request, equipe_id):
    equipe = get_object_or_404(Equipe, pk=equipe_id)
    equipe.delete()
    return redirect('equipe_list')

@login_required
def historico(request):
    if request.method == 'POST':
        if "equipe_list" in request.POST:
            return redirect('equipe_list')
        elif "jogador_list" in request.POST:
            return redirect('jogador_list')
        elif "substituicao_list" in request.POST:
            return redirect('substituicao_list')
        elif "tecnico_list" in request.POST:
            return redirect('tecnico_list')
        elif "escalacao_list" in request.POST:
            return redirect('escalacao_list')
        elif "campeonato_list" in request.POST:
            return redirect('campeonato_list')
        elif "partida_list" in request.POST:
            return redirect('partida_list')
        elif "desempenho_list" in request.POST:
            return redirect('desempenho_list')
        elif "estadio_list" in request.POST:
            return redirect('estadio_list')
    return render(request, 'historico.html')

@login_required
def estadio(request):
    if request.method == 'POST':
        form = EstadioForm(request.POST)
        if form.is_valid():
            estadio_instance = form.save()
            return redirect('estadio_list')
    else:
        form = EstadioForm()
    return render(request, 'userpage.html', {'form': form})

def estadio_list(request):
    estadio_list = Estadio.objects.all()
    return render(request, 'estadio_list.html', {'estadio_list': estadio_list})

@login_required
def editar_estadio(request, estadio_id):
    estadio = get_object_or_404(Estadio, pk=estadio_id)
    
    if request.method == 'POST':
        form = EstadioForm(request.POST, instance=estadio)
        if form.is_valid():
            form.save()
            return redirect('estadio_list')
    else:
        form = EstadioForm(instance=estadio)

    return render(request, 'editar_estadio.html', {'form': form})

@login_required
def excluir_estadio(request, estadio_id):
    estadio = get_object_or_404(Estadio, pk=estadio_id)
    estadio.delete()
    return redirect('estadio_list')

@login_required
def tecnico(request):
    if request.method == 'POST':
        form = TecnicoForm(request.POST)
        if form.is_valid():
            tecnico_instance = form.save(commit=False)
            tecnico_instance.user = request.user
            tecnico_instance.save()
            return redirect('tecnico_list')
    else:
        form = TecnicoForm()

    return render(request, 'userpage.html', {'form': form})


def tecnico_list(request):
    tecnico_list = Tecnico.objects.all()
    return render(request, 'tecnico_list.html', {'tecnico_list': tecnico_list})

@login_required
def editar_tecnico(request, tecnico_id):
    tecnico = get_object_or_404(Tecnico, pk=tecnico_id)
    
    if request.method == 'POST':
        form = TecnicoForm(request.POST, instance=tecnico)
        if form.is_valid():
            form.save()
            return redirect('tecnico_list')
    else:
        form = TecnicoForm(instance=tecnico)

    return render(request, 'editar_tecnico.html', {'form': form})

@login_required
def excluir_tecnico(request, tecnico_id):
    tecnico = get_object_or_404(Tecnico, pk=tecnico_id)
    tecnico.delete()
    return redirect('tecnico_list')

@login_required
def campeonato(request):
    if request.method == 'POST':
        form = CampeonatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('campeonato_list')
    else:
        form = CampeonatoForm()

    return render(request, 'userpage.html', {'form': form})

def campeonato_list(request):
    campeonato_list = Campeonato.objects.all()
    return render(request, 'campeonato_list.html', {'campeonato_list': campeonato_list})

@login_required
def editar_campeonato(request, campeonato_id):
    campeonato = get_object_or_404(Campeonato, pk=campeonato_id)
    
    if request.method == 'POST':
        form = CampeonatoForm(request.POST, instance=campeonato)
        if form.is_valid():
            form.save()
            return redirect('campeonato_list')
    else:
        form = CampeonatoForm(instance=campeonato)

    return render(request, 'editar_campeonato.html', {'form': form})

@login_required
def excluir_campeonato(request, campeonato_id):
    campeonato = get_object_or_404(Campeonato, pk=campeonato_id)
    campeonato.delete()
    return redirect('campeonato_list')

@login_required
def jogador(request):
    if request.method == 'POST':
        form = JogadorForm(request.POST)
        if form.is_valid():
            jogador_instance = form.save(commit=False)
            jogador_instance.user = request.user
            jogador_instance.save()
            return redirect('jogador_list')
    else:
        form = JogadorForm()

    return render(request, 'userpage.html', {'form': form})  # Altere o template conforme necessário

def jogador_list(request):
    jogador_list = Jogador.objects.all()
    return render(request, 'jogador_list.html', {'jogador_list': jogador_list})

@login_required
def editar_jogador(request, jogador_id):
    jogador = get_object_or_404(Jogador, pk=jogador_id)
    
    if request.method == 'POST':
        form = JogadorForm(request.POST, instance=jogador)
        if form.is_valid():
            form.save()
            return redirect('jogador_list')
    else:
        form = JogadorForm(instance=jogador)

    return render(request, 'editar_jogador.html', {'form': form})

@login_required
def excluir_jogador(request, jogador_id):
    jogador = get_object_or_404(Jogador, pk=jogador_id)
    jogador.delete()
    return redirect('jogador_list')

@login_required
def desempenho(request):
    if request.method == 'POST':
        form = DesempenhoForm(request.POST)
        if form.is_valid():
            desempenho_instance = form.save(commit=False)
            desempenho_instance.save()
            return redirect('desempenho_list')
    else:
        form = DesempenhoForm()

    return render(request, 'userpage.html', {'form': form})

def desempenho_list(request):
    desempenho_list = Desempenho.objects.all()
    return render(request, 'desempenho_list.html', {'desempenho_list': desempenho_list})

@login_required
def editar_desempenho(request, desempenho_id):
    desempenho = get_object_or_404(Desempenho, pk=desempenho_id)
    
    if request.method == 'POST':
        form = DesempenhoForm(request.POST, instance=desempenho)
        if form.is_valid():
            form.save()
            return redirect('desempenho_list')
    else:
        form = DesempenhoForm(instance=desempenho)

    return render(request, 'editar_desempenho.html', {'form': form})

@login_required
def excluir_desempenho(request, desempenho_id):
    desempenho = get_object_or_404(Desempenho, pk=desempenho_id)
    desempenho.delete()
    return redirect('desempenho_list')


@login_required
def partida(request):
    if request.method == 'POST':
        form = PartidaForm(request.POST)
        if form.is_valid():
            partida_instance = form.save(commit=False)
            partida_instance.save()
            return redirect('partida_list')
    else:
        form = PartidaForm()

    return render(request, 'userpage.html', {'form': form})

def partida_list(request):
    partida_list = Partida.objects.all()
    return render(request, 'partida_list.html', {'partida_list': partida_list})

@login_required
def editar_partida(request, partida_id):
    partida = get_object_or_404(Partida, pk=partida_id)
    
    if request.method == 'POST':
        form = PartidaForm(request.POST, instance=partida)
        if form.is_valid():
            form.save()
            return redirect('partida_list')
    else:
        form = PartidaForm(instance=partida)

    return render(request, 'editar_partida.html', {'form': form})

@login_required
def excluir_partida(request, partida_id):
    partida = get_object_or_404(Partida, pk=partida_id)
    partida.delete()
    return redirect('partida_list')

@login_required
def escalacao(request):
    if request.method == 'POST':
        form = EscalacaoForm(request.POST)
        if form.is_valid():
            escalacao_instance = form.save(commit=False)
            escalacao_instance.save()
            return redirect('escalacao_list')
    else:
        form = EscalacaoForm()

    return render(request, 'userpage.html', {'form': form})

def escalacao_list(request):
    escalacao_list = Escalacao.objects.all()
    return render(request, 'escalacao_list.html', {'escalacao_list': escalacao_list})

@login_required
def editar_escalacao(request, escalacao_id):
    escalacao = get_object_or_404(Escalacao, pk=escalacao_id)
    
    if request.method == 'POST':
        form = EscalacaoForm(request.POST, instance=escalacao)
        if form.is_valid():
            form.save()
            return redirect('escalacao_list')
    else:
        form = EscalacaoForm(instance=escalacao)

    return render(request, 'editar_escalacao.html', {'form': form})

@login_required
def excluir_escalacao(request, escalacao_id):
    escalacao = get_object_or_404(Escalacao, pk=escalacao_id)
    escalacao.delete()
    return redirect('escalacao_list')

@login_required
def substituicao(request):
    if request.method == 'POST':
        form = SubstituicaoForm(request.POST)
        if form.is_valid():
            substituicao_instance = form.save(commit=False)
            substituicao_instance.save()
            return redirect('substituicao_list')
    else:
        form = SubstituicaoForm()

    return render(request, 'userpage.html', {'form': form})

def substituicao_list(request):
    substituicao_list = Substituicao.objects.all()
    return render(request, 'substituicao_list.html', {'substituicao_list': substituicao_list})

@login_required
def editar_substituicao(request, substituicao_id):
    substituicao = get_object_or_404(Substituicao, pk=substituicao_id)
    
    if request.method == 'POST':
        form = SubstituicaoForm(request.POST, instance=substituicao)
        if form.is_valid():
            form.save()
            return redirect('substituicao_list')
    else:
        form = SubstituicaoForm(instance=substituicao)

    return render(request, 'editar_substituicao.html', {'form': form})

@login_required
def excluir_substituicao(request, substituicao_id):
    substituicao = get_object_or_404(Substituicao, pk=substituicao_id)
    substituicao.delete()
    return redirect('substituicao_list')
