from django.contrib.admin import ModelAdmin, register

from apps.aperitivo.models import Video


@register(Video)
class VideoAdmin(ModelAdmin):
    list_display = ('titulo', 'slug', 'creation', 'youtube_id', )
    ordering = ('creation', )
    # Amarra o campo slug ao campo Titulo de de forma que valores do campo titulo sejam preenchidos em tempo real
    # no momento de preenchimento do titulo, mas campo slug deve ser do tipo SlugField.
    prepopulated_fields = {'slug': ('titulo',)}
