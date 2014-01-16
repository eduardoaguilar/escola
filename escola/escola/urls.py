from django.conf.urls import * #patterns, include, url
from django.conf import settings 

from django.contrib import admin
admin.autodiscover()

from curso.models  import Aluno, Turma
    
urlpatterns = patterns('',
    #(r'^$', "escola_novo.curso.views.lista"),
    (r'^$', "curso.views.inicio"),
    #controle aluno
    (r'^adicionaAluno/$', "curso.views.adicionaAluno"),
    (r'^listaAluno/$', "curso.views.listaAluno"),
    (r'^itemAluno/(?P<nr_item>\d+)/$',"curso.views.itemAluno"),
    (r'^removeAluno/(?P<nr_item>\d+)/$',"curso.views.removeAluno"),
    
    #controle local
    (r'^adicionaLocal/$', "curso.views.adicionaLocal"),
    (r'^listaLocal/$', "curso.views.listaLocal"),
    (r'^itemLocal/(?P<nr_item>\d+)/$',"curso.views.itemLocal"),
    (r'^removeLocal/(?P<nr_item>\d+)/$',"curso.views.removeLocal"),
    
    #controle Cursos
    (r'^adicionaCurso/$', "curso.views.adicionaCurso"),
    (r'^listaCurso/$', "curso.views.listaCurso"),
    (r'^itemCurso/(?P<nr_item>\d+)/$',"curso.views.itemCurso"),
    (r'^removeCurso/(?P<nr_item>\d+)/$',"curso.views.removeCurso"),
    
    #controle Turmas
    (r'^adicionaTurma/$', "curso.views.adicionaTurma"),
    (r'^listaTurma/$', "curso.views.listaTurma"),
    (r'^itemTurma/(?P<nr_item>\d+)/$',"curso.views.itemTurma"),
    (r'^removeTurma/(?P<nr_item>\d+)/$',"curso.views.removeTurma"),
    
    #controle matricula
    (r'^adicionaMatricula/$', "curso.views.adicionaMatricula"),
    (r'^listaMatricula/$', "curso.views.listaMatricula"),
    (r'^itemMatricula/(?P<nr_item>\d+)/$',"curso.views.itemMatricula"),
    (r'^removeMatricula/(?P<nr_item>\d+)/$',"curso.views.removeMatricula"),
    
    (r'^login/',"django.contrib.auth.views.login", {"template_name": "login.html"}),
    (r'^logout/',"django.contrib.auth.views.logout_then_login", {'login_url':'/login/'}), # chama essa page quando fizer o login .tem q passar como parametro              
    url(r'^admin/', include(admin.site.urls)),
    )

if settings.DEBUG:
    urlpatterns += patterns('',
         (r'^media/(?P<path>.*)$', 'django.views.static.serve',
             {'document_root': settings.MEDIA_ROOT}),
    )
    