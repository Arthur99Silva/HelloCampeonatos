from django.db import models

class Tecnico(models.Model):
    nome = models.TextField()
    nacionalidade = models.TextField()
    naturalidade = models.TextField()

    def __str__(self):
        return f'{self.nome} - Nacionalidade: {self.nacionalidade} - Naturalidade: {self.naturalidade}'
    
class Campeonato(models.Model):
    nome = models.TextField()
    ano = models.IntegerField()
    serie = models.CharField(max_length=1)

    def __str__(self):
        return f'{self.nome} - {self.ano} - Série {self.serie}'

class Estadio(models.Model):
    nome_estadio = models.TextField(unique=True)
    pais = models.TextField()
    estado = models.TextField()
    cidade = models.TextField()
    capacidade = models.IntegerField()

    def __str__(self):
        return f'{self.nome_estadio} - {self.cidade}, {self.estado}, {self.pais}'

class Equipe(models.Model):
    nome = models.TextField(unique=True)
    sigla = models.CharField(max_length=3, unique=True)
    cidade = models.TextField(blank=True, null=True)
    estado = models.TextField(blank=True, null=True)
    tecnico = models.ForeignKey('Tecnico', on_delete=models.CASCADE)
    estadio = models.ForeignKey('Estadio', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome} ({self.sigla}) - {self.cidade}, {self.estado} - Técnico: {self.tecnico.nome} - Estádio: {self.estadio.nome_estadio}'


class Jogador(models.Model):
    POSICOES_CHOICES = [
        ('CA', 'Centroavante'),
        ('MA', 'Meia Atacante'),
        ('AD', 'Avançado Direito'),
        ('MC', 'Meio de Campo Central'),
        ('ME', 'Meia Esquerda'),
        ('LE', 'Lateral Esquerdo'),
        ('ZC', 'Zagueiro Central'),
        ('LD', 'Lateral Direito'),
        ('GL', 'Goleiro'),
        ('VO', 'Volante'),
        ('AE', 'Avançado Esquerdo'),
    ]

    nome = models.TextField()
    num_camisa = models.IntegerField()
    idade = models.IntegerField(default=0)
    equipe = models.ForeignKey('Equipe', on_delete=models.CASCADE) 
# Campo adicional para a opção selecionada
    posicao = models.CharField(max_length=2, choices=POSICOES_CHOICES, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Ao salvar o objeto Jogador, atualize posicao_selecionada para a posição escolhida
        self.posicao = self.posicao
        super().save(*args, **kwargs)


    def __str__(self):
        return f'{self.nome} - Camisa {self.num_camisa} - {self.equipe.nome} - Equipe {self.equipe.nome} - {self.equipe.sigla}'

class Partida(models.Model):
    data = models.DateField()
    hora = models.TimeField()
    equipe_casa_id = models.ForeignKey(Equipe, related_name='partidas_casa', on_delete=models.CASCADE)
    placar_casa = models.IntegerField(default=0)
    equipe_visitante_id = models.ForeignKey(Equipe, related_name='partidas_visitante', on_delete=models.CASCADE)
    placar_visitante = models.IntegerField(default=0)
    arbitro = models.IntegerField()
    qtd_publico = models.IntegerField(default=0)
    campeonato = models.ForeignKey(Campeonato, on_delete=models.CASCADE)
    status = models.IntegerField()
    estadio_id = models.ForeignKey(Estadio, on_delete=models.CASCADE)
    rodada = models.IntegerField()
    turno = models.IntegerField()

    def __str__(self):
        return f'{self.equipe_casa_id.nome} {self.placar_casa} - {self.equipe_visitante_id.nome} {self.placar_visitante} - {self.campeonato.ano}'

class Escalacao(models.Model):
    partida_fk = models.ForeignKey(Partida, on_delete=models.CASCADE)
    jogador_fk = models.ForeignKey(Jogador, on_delete=models.CASCADE)
    titular = models.IntegerField()

    def __str__(self):
        return f'{self.jogador_fk.nome} - {self.partida_fk} - {"Titular" if self.titular else "Reserva"}'

class Desempenho(models.Model):
    id = models.AutoField(primary_key=True)
    jogador_id = models.ForeignKey(Jogador, on_delete=models.CASCADE)
    partida_id = models.ForeignKey(Partida, on_delete=models.CASCADE)
    gols = models.IntegerField(default=0)
    cartao_amarelo = models.IntegerField(default=0)
    cartao_vermelho = models.IntegerField(default=0)
    faltas_cometidas = models.IntegerField(default=0)
    faltas_recebidas = models.IntegerField(default=0)
    defesas = models.IntegerField(default=0)
    chutes_a_gol = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.jogador_id.nome} - {self.partida_id} - Gols: {self.gols}'

class Escalacao(models.Model):
    id = models.AutoField(primary_key=True)
    jogador_id = models.ForeignKey(Jogador, on_delete=models.CASCADE)
    partida_id = models.ForeignKey(Partida, on_delete=models.CASCADE)
    titular = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.jogador_id.nome} - {self.partida_id} - Titular: {self.titular}'

class Substituicao(models.Model):
    id = models.AutoField(primary_key=True)
    saindo_jogador_id = models.ForeignKey(Jogador, related_name='substituicoes_saindo', on_delete=models.CASCADE)
    entrando_jogador_id = models.ForeignKey(Jogador, related_name='substituicoes_entrando', on_delete=models.CASCADE)
    min_partida = models.IntegerField()
    partida_id = models.ForeignKey(Partida, on_delete=models.CASCADE)

    def __str__(self):
        return f'Substituição: {self.saindo_jogador_id.nome} por {self.entrando_jogador_id.nome} - Partida: {self.partida_id}'