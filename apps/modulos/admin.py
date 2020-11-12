from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin

from apps.modulos.models import Modulo, Aula


@admin.register(Modulo)
class ModuloAdmin(OrderedModelAdmin):
    list_display = ('titulo', 'publico', 'move_up_down_links')
    # Amarra o campo slug ao campo Titulo de de forma que valores do campo titulo sejam preenchidos em tempo real
    # no momento de preenchimento do titulo, mas campo slug deve ser do tipo SlugField.
    prepopulated_fields = {'slug': ('titulo',)}


@admin.register(Aula)
class AulaAdmin(OrderedModelAdmin):
    list_display = ('titulo', 'modulo', 'order', 'move_up_down_links')
    list_filter = ('modulo', )
    ordering = ('modulo', 'order')
    # Amarra o campo slug ao campo Titulo de de forma que valores do campo titulo sejam preenchidos em tempo real
    # no momento de preenchimento do titulo, mas campo slug deve ser do tipo SlugField.
    prepopulated_fields = {'slug': ('titulo',)}
