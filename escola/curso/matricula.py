# _*_ encondig: utf-8 _*_


from django.shortcuts import render_to_response  , get_object_or_404 , render
from django.http import HttpResponseRedirect
from models import Aluno, Local, Curso, Turma, Matricula, Periodo
from forms import FormAluno, FormItemLocal, FormItemCurso , FormTurma, FormMatricula
from django.contrib import messages
from django.http.response import HttpResponseRedirect, HttpResponse
import datetime

from django.contrib.auth.decorators import login_required, user_passes_test, \
    permission_required
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.http.response import HttpResponse
import datetime
from datetime import timedelta


from django.template import RequestContext
from django.views.generic import ListView

nome_relatorio = "relatorio_matricula"

@login_required
def listaMatricula(request):
    lista = Matricula.objects.all
    if request.method =="POST":
        curso = request.POST['curso']
        local = request.POST['local']
        periodo = request.POST['periodo']
        aluno = request.POST['aluno']
        lista = Matricula.objects.all().filter(nmTurma__nmCurso__nmCurso__icontains=curso, nmTurma__nmLocal__nmLocal__icontains=local,nmTurma__nmPeriodo__nmPeriodo__icontains=periodo,nmAluno__nmAluno__icontains=aluno)
        
    return render_to_response ("matricula/listaMatricula.html", {"lista": lista},
        context_instance=RequestContext(request)) 
    
@login_required
def adicionaMatricula (request):
    turma = Turma.objects.all()
    aluno = Aluno.objects.all()
    periodo = Periodo.objects.all()
    if request.method == "POST":
        form = FormMatricula (request.POST)
        if form.is_valid ():
            form.save()
            return HttpResponseRedirect("/listaMatricula/")
    else:
        form = FormMatricula()  
    return render_to_response ('matricula/adicionaMatricula.html', {"form":form, "turma":turma, "aluno":aluno,"periodo":periodo}, context_instance=RequestContext(request))  

@login_required
def itemMatricula(request, nr_item): 
    turma = Turma.objects.all()
    aluno = Aluno.objects.all()
    item = get_object_or_404 (Matricula, pk=nr_item)   
    if request.method == "POST":
        form = FormMatricula (request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/itemMatricula/" + str(nr_item) + "/")
        else:
            messages.add_message(request, messages.WARNING, 'ERRO NA EDICAO')
    else:
        form = FormMatricula(instance=item)
    return render_to_response ('matricula/itemMatricula.html', {"form":form, "turma":turma, "aluno":aluno}, context_instance=RequestContext(request))
    
@login_required
def removeMatricula(request, nr_item):
    item = get_object_or_404 (Matricula, pk=nr_item) 
    if request.method == "POST":
        item.delete() 
        messages.add_message(request, messages.WARNING, 'MATRICULA REMOVIDA')
        return HttpResponseRedirect("/listaMatricula/")
    return render_to_response ("matricula/removeMatricula.html", {'item':item}, context_instance=RequestContext(request))



