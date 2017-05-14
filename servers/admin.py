from django.contrib import admin

from .models import Server

class Serverdmin(admin.ModelAdmin):
    list_display = ['nome_do_jogo', 'porta_do_jogo', 'connect', 'run']
    ordering = ['nome_do_jogo']

admin.site.register(Server, Serverdmin)
