# -*- coding: utf-8 -*-
import os
from django.shortcuts import render
from django.http import HttpResponse


def server_start(request):
    os.system('C:\\steamcmd\servers\{0}\start.bat'.format(request.GET.get('pasta')))
    return HttpResponse('Iniciando servidor...')

def server_stop(request):
    os.system('C:\\steamcmd\servers\{0}\stop.bat'.format(request.GET.get('pasta')))
    return HttpResponse('Fechando servidor...')
