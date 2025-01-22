from django.db import models
from django.utils import timezone # função timezone para pegar a data da criação

# Create your models here.

LISTA_CATEGORIAS = (
    # (informação a ser armazenada no banco de dados , informação que vai aparecer ao usuário ),
    ("ANALISES", "Análises"),
    ("PROGRAMACAO", "Programação"),
    ("APRESENTACAO", "Apresentação"),
    ("OUTROS", "Outros"),
)

# Criar o Filme 
class Filme(models.Model):
    titulo = models.CharField(max_length=100) # Charfield é um campo de texto pequeno
    thumb = models.ImageField(upload_to='thumb_filmes') # quando a pessoa criar um filme, vai ter que fazer upload dessa imagem, e a imagem vai ser armazenada na pasta THUMB_FILMES
    descricao = models.TextField(max_length=1000) # textfield é um campo de texto maior
    categoria = models.CharField(max_length=15, choices = LISTA_CATEGORIAS) # choices são as opções pra essa variavel
    visualizacoes = models.IntegerField(default=0) # IntegerField é um valor numérico
    data_criacao = models.DateTimeField(default=timezone.now) # datetimefield é o formato de data com horario.   //   função timezone para pegar a data da criação
    
    def __str__(self):
        return self.titulo



# criar os episodios