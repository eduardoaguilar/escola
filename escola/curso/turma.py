from django.shortcuts import render_to_response  , get_object_or_404 , render
from django.http import HttpResponseRedirect
from models import Aluno, Local, Curso, Turma, Matricula, Periodo
from forms import FormTurma
from django.contrib import messages
from django.http.response import HttpResponseRedirect, HttpResponse
import datetime
from django.contrib.auth.decorators import login_required, user_passes_test, \
    permission_required

from django.template.context import RequestContext
from datetime import timedelta

from django.template import RequestContext
from django.views.generic import ListView
import json

nome_relatorio = "relatorio_turma"

@login_required
def listaTurma(request):
    lista = Turma.objects.all()
    if request.method == "POST":
        curso = request.POST['curso']
        local = request.POST['local']
        periodo = request.POST['periodo']
        lista = Turma.objects.all().filter(nmCurso__nmCurso__icontains=curso, nmLocal__nmLocal__icontains=local, nmPeriodo__nmPeriodo__icontains=periodo)
    lista = lista.order_by('nmCurso', 'nmLocal', 'nmPeriodo')
    request.session['relatorio_turma'] = lista
    return render_to_response ("turma/listaTurma.html", {'lista': lista},
        context_instance=RequestContext(request))  # para funcionar o icone da lixeira. adciona a configuracao media_url

@login_required
def adicionaTurma (request):
    curso = Curso.objects.all()
    local = Local.objects.all()
    periodo = Periodo.objects.all()
    
    if request.method == "POST":
        print request.POST['tbCurso']
        print request.POST['tbLocal']
        print request.POST['tbPeriodo']
    
        f_turma = Turma (
                        # id = models.AutoField(primary_key=True)
                        nmCurso=Curso.objects.get(pk=request.POST['tbCurso']),
                        nmLocal=Local.objects.get(pk=request.POST['tbLocal']),
                        nmPeriodo=Periodo.objects.get(pk=request.POST['tbPeriodo'])
                         )
        f_turma.save()
        
        return HttpResponseRedirect("/listaTurma/")
    return render_to_response ('turma/adicionaTurma.html', {'curso':curso, 'local':local, 'periodo':periodo}, context_instance=RequestContext(request))  # essa linha eh um mecansmo de proteao

@login_required
def itemTurma(request, nr_item):  # nr_item se refere ao id da Turma
    l_curso = Curso.objects.all()
    l_local = Local.objects.all()
    l_periodo = Periodo.objects.all()
    l_turma = get_object_or_404 (Turma, pk=nr_item)   
   
    if request.method == "POST":
        f_turma = Turma(
                id=l_turma.id ,
                nmCurso=Curso.objects.get(pk=request.POST['curso']),
                nmLocal=Local.objects.get(pk=request.POST['local']),
                nmPeriodo=Periodo.objects.get(pk=request.POST['periodo'])
                )
        f_turma.save()
        return HttpResponseRedirect("/itemTurma/" + str(nr_item) + "/")
    return render_to_response ("turma/itemTurma.html", {'turma':l_turma, "curso":l_curso, "local":l_local, "periodo":l_periodo}, context_instance=RequestContext(request))
    
@login_required
def ListaAlunosMatriculados(request, nr_item):  # nr_item se refere ao id da Turma
    lista = Matricula.objects.all().filter(nmTurma=nr_item)
    request.session['relatorio_turma'] = lista
    
    return render_to_response ("matricula/listaAlunosMatriculados.html", {"lista": lista},
        context_instance=RequestContext(request)) 



@login_required
def removeTurma(request, nr_item):
    item = get_object_or_404 (Turma, pk=nr_item) 
    if request.method == "POST":
        item.delete() 
        messages.add_message(request, messages.WARNING, 'TURMA REMOVIDA')
        return HttpResponseRedirect("/listaTurma/")
    return render_to_response ("turma/removeTurma.html", {'item':item}, context_instance=RequestContext(request))

