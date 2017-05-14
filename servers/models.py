from __future__ import unicode_literals
from django.db import models
import os

# Create your models here.
class Server(models.Model):
    nome_do_jogo = models.CharField(max_length=200)
    porta_do_jogo = models.CharField(max_length=10)
    pasta_do_server = models.CharField(max_length=255)

    def connect(self):
        return '<a href="steam://connect/192.168.1.200:{0}">Entrar no steam</a>'.format(self.porta_do_jogo)
    connect.short_description = 'Entrar no servidor'
    connect.is_safe = True
    connect.allow_tags = True
    
    def run(self):
        html = ''
        run = os.system('C:\steamcmd\servers\{0}\show.bat'.format(self.pasta_do_server))
        if run == 1:
            html = '''
            <script src='http://static.4gamerz.com.br/js/jquery.js'></script>
            <script>
                $( document ).ready(function() {

                      $( "#iniciar" ).click(function() {
                          alert( 'Iniciando servidor...' );
                          $.get( "/server-start/?pasta=''' +self.pasta_do_server+'''", function( data ) {                          });
                          
                      });
                  });
            </script>
            <span style='color:red'>Fechado</span> - <a href='#' id="iniciar">Iniciar</a>
            '''
        else:
            html = '''
            <script src='http://static.4gamerz.com.br/js/jquery.js'></script>
            <script>
            $( document ).ready(function() {


                  $( "#fechar" ).click(function() {
                     alert( 'Fechando servidor...' );
                      $.get( "/server-stop/?pasta=''' +self.pasta_do_server+'''", function( data ) {});
                      location.href= '/admin/servers/server/';
                  });
            });
            </script>
            <span style='color:green'>Aberto</span> - <a href='#' id="fechar">Fechar</a>
            '''
        return html
    run.short_description = "Estado do Server"
    run.is_safe = True
    run.allow_tags = True
