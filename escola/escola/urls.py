from django.conf.urls import * #patterns, include, url
from django.conf import settings 

from django.contrib import admin
admin.autodiscover()

from curso.models  import Aluno, Turma
    
urlpatterns = patterns('',
    #(r'^$', "escola_novo.curso.views.lista"),
    (r'^$', "curso.views.inicio"),
    #controle aluno
    (r'^adicionaAluno/$', "curso.aluno.adicionaAluno"),
    (r'^listaAluno/$', "curso.aluno.listaAluno"),
    (r'^itemAluno/(?P<nr_item>\d+)/$',"curso.aluno.itemAluno"),
    (r'^removeAluno/(?P<nr_item>\d+)/$',"curso.aluno.removeAluno"),
    (r'^ListaTurmasdoAluno/(?P<id>\d+)/$',"curso.aluno.ListaTurmasdoAluno"),
    
    #controle local
    (r'^adicionaLocal/$', "curso.views.adicionaLocal"),
    (r'^listaLocal/$', "curso.views.listaLocal"),
    (r'^itemLocal/(?P<nr_item>\d+)/$',"curso.views.itemLocal"),
    (r'^removeLocal/(?P<nr_item>\d+)/$',"curso.views.removeLocal"),
    
    #controle Cursos
    (r'^adicionaCurso/$', "curso.curso.adicionaCurso"),
    (r'^listaCurso/$', "curso.curso.listaCurso"),
    (r'^itemCurso/(?P<nr_item>\d+)/$',"curso.curso.itemCurso"),
    (r'^removeCurso/(?P<nr_item>\d+)/$',"curso.curso.removeCurso"),
    
    #controle Turmas
    (r'^adicionaTurma/$', "curso.turma.adicionaTurma"),
    (r'^listaTurma/$', "curso.turma.listaTurma"),
    (r'^itemTurma/(?P<nr_item>\d+)/$',"curso.turma.itemTurma"),
    (r'^removeTurma/(?P<nr_item>\d+)/$',"curso.turma.removeTurma"),
    (r'^ListaAlunosMatriculados/(?P<nr_item>\d+)/$',"curso.turma.ListaAlunosMatriculados"),
    
    
    #controle matricula
    (r'^adicionaMatricula/$', "curso.matricula.adicionaMatricula"),
    (r'^listaMatricula/$', "curso.matricula.listaMatricula"),
    (r'^itemMatricula/(?P<nr_item>\d+)/$',"curso.matricula.itemMatricula"),
    (r'^removeMatricula/(?P<nr_item>\d+)/$',"curso.matricula.removeMatricula"),
    #controle periodo
    (r'^adicionaPeriodo/$', "curso.views.adicionaPeriodo"),
    (r'^listaPeriodo/$', "curso.views.listaPeriodo"),
    
    
    (r'^login/',"django.contrib.auth.views.login", {"template_name": "login.html"}),
    (r'^logout/',"django.contrib.auth.views.logout_then_login", {'login_url':'/login/'}), # chama essa page quando fizer o login .tem q passar como parametro              
    url(r'^admin/', include(admin.site.urls)),
    )

if settings.DEBUG:
    urlpatterns += patterns('',
         (r'^media/(?P<path>.*)$', 'django.views.static.serve',
             {'document_root': settings.MEDIA_ROOT}),
    )
    