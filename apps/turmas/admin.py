from django.contrib import admin
from .models import Turma


class MatriculaInline(admin.TabularInline):
    # Configuraçao da relação Turma e Aluno a ser configurada para visualização
    model = Turma.alunos.through
    # Um form extra dentro do admin no contexto da MatriculaInline
    extra = 1
    # Mostrar campo somente como leitura
    readonly_fields = ('data',)
    # Mostrar campo de busca como autocomplete
    autocomplete_fields = ('usuario',)
    # Ordenando em forma decrescente
    ordering = ('-data',)


@admin.register(Turma)
class TurmasAdmin(admin.ModelAdmin):
    # Conf para visualização na class MatriculaInline no admin
    inlines = [MatriculaInline]
    list_display = ('nome', 'slug', 'inicio', 'fim', )
    prepopulated_fields = {'slug': ('nome',)}
    ordering = ('-inicio',)
