from django import forms
from django.contrib.auth import get_user_model
from django import forms
from .models import Tecnico, Campeonato, Estadio, Equipe, Jogador, Partida, Escalacao, Desempenho, Substituicao

class TecnicoForm(forms.ModelForm):
    class Meta:
        model = Tecnico
        fields = '__all__'

class UserUpdateForm(forms.ModelForm):
    class Meta:
        fields = ('first_name', 'username', 'password')
        model = get_user_model()

class CampeonatoForm(forms.ModelForm):
    class Meta:
        model = Campeonato
        fields = '__all__'

class EstadioForm(forms.ModelForm):
    class Meta:
        model = Estadio
        fields = '__all__'

class EquipeForm(forms.ModelForm):
    estadio = forms.ModelChoiceField(
        queryset=Estadio.objects.all(),
        empty_label="Selecione um estádio",
        label="Estádio"
    )
    tecnico = forms.ModelChoiceField(
        queryset=Tecnico.objects.all(),
        empty_label="Selecione um técnico",
        label="Técnico"
    )
    class Meta:
        model = Equipe
        fields = '__all__'

class JogadorForm(forms.ModelForm):
    equipe = forms.ModelChoiceField(
        queryset=Equipe.objects.all(),
        empty_label="Selecione uma equipe",
        label="Equipe"
    )
    class Meta:
        model = Jogador
        fields = '__all__'

class PartidaForm(forms.ModelForm):
    equipe_casa = forms.ModelChoiceField(
        queryset=Equipe.objects.all(),
        empty_label="Selecione uma equipe",
        label="Equipe Casa"
    )

    equipe_visitante = forms.ModelChoiceField(
        queryset=Equipe.objects.all(),
        empty_label="Selecione uma equipe",
        label="Equipe Visitante"
    )

    estadio = forms.ModelChoiceField(
        queryset=Estadio.objects.all(),
        empty_label="Selecione um estádio",
        label="Estádio"
    )

    campeonato = forms.ModelChoiceField(
        queryset=Campeonato.objects.all(),
        empty_label="Selecione um campeonato",
        label="Campeonato"
    )

    class Meta:
        model = Partida
        fields = '__all__'


class EscalacaoForm(forms.ModelForm):
    jogador = forms.ModelChoiceField(
        queryset=Jogador.objects.all(),
        empty_label="Selecione um jogador",
        label="Jogador"
    )

    partida = forms.ModelChoiceField(
        queryset=Partida.objects.all(),
        empty_label="Selecione uma partida",
        label="Partida"
    )

    titular = forms.BooleanField(
        label="Titular",
        required=False,
        initial=False
    )

    class Meta:
        model = Escalacao
        fields = '__all__'

class DesempenhoForm(forms.ModelForm):
    id_jogador_fk = forms.ModelChoiceField(
        queryset=Jogador.objects.all(),
        empty_label="Selecione um jogador",
        label="Jogador"
    )

    id_partida_fk = forms.ModelChoiceField(
        queryset=Partida.objects.all(),
        empty_label="Selecione uma partida",
        label="Partida"
    )

    class Meta:
        model = Desempenho
        fields = '__all__'

class SubstituicaoForm(forms.ModelForm):
    saindo_jogador_id = forms.ModelChoiceField(
        queryset=Jogador.objects.all(),
        empty_label="Selecione um jogador",
        label="Saindo Jogador"
    )

    entrando_jogador_id = forms.ModelChoiceField(
        queryset=Jogador.objects.all(),
        empty_label="Selecione um jogador",
        label="Entrando Jogador"
    )

    partida_id = forms.ModelChoiceField(
        queryset=Partida.objects.all(),
        empty_label="Selecione uma partida",
        label="Partida"
    )

    class Meta:
        model = Substituicao
        fields = '__all__'



