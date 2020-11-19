from django.contrib.auth import get_user_model
from django.db import models


class Turma(models.Model):
    nome = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    inicio = models.DateField()
    fim = models.DateField()
    # Campo alunos recebe a relação User e Turma com intermediação da tabela Matricula.
    # Dessa forma temos mais controle no add de campos na tabela Matricula.
    alunos = models.ManyToManyField(get_user_model(), through='Matricula')


class Matricula(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    turma = models.ForeignKey(Turma, on_delete=models.CASCADE)

    # Classe Meta é a classe responsável apenas pelas configurações da class do Model. Ex: Matricula
    class Meta:
        # São únicos os dois campos se usados em conjunto. Ex. Aluno só poderar se matricular em uma turma.
        unique_together = [['usuario', 'turma']]
        # Ordena a tabela por turma e em seguida por data. Ex. Matriculas da mesma
        # turma serão ordenadas por data.
        ordering = ['turma', 'data']
