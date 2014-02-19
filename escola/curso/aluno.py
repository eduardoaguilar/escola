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

nome_relatorio = "relatorio_aluno"

@login_required
def listaAluno(request):
    lista = Aluno.objects.all()
    if request.method == "POST":
        aluno = request.POST['aluno']
        lista = Aluno.objects.all().filter(nmAluno__icontains=aluno)
    lista = lista.order_by('nmAluno')
    request.session['relatorio_aluno'] = lista
    return render_to_response ("aluno/listaAluno.html", {'lista': lista}, context_instance=RequestContext(request)) 

@login_required
def adicionaAluno (request):
    warning = True
    if request.method == "POST":
        if validacao(request):
            f_aluno = Aluno(
                    nmAluno=request.POST['nmAluno'],
                    dtMatricula=datetime.datetime.now(),
                    )
            f_aluno.save()
        return HttpResponseRedirect ("/adicionaAluno/")
    return render_to_response ("aluno/adicionaAluno.html", context_instance=RequestContext(request))  
@login_required
def itemAluno(request, nr_item):                   
    item = get_object_or_404 (Aluno, pk=nr_item)   
    if request.method == "POST":
        f_aluno = Aluno(
                    id=item.id,
                    nmAluno=request.POST['nmAluno'],
                    dtMatricula=item.dtMatricula ,)
        f_aluno.save()
        return HttpResponseRedirect ("/itemAluno/" + str(nr_item) + "/")
    return render_to_response ('aluno/itemAluno.html', {"aluno":item}, context_instance=RequestContext(request))
            
@login_required
def removeAluno(request, nr_item):
    warning = True
    item = get_object_or_404 (Aluno, pk=nr_item) 
    if request.method == "POST":
        item.delete() 
        messages.add_message(request, messages.WARNING, 'ALUNO REMOVIDO')
        return HttpResponseRedirect("/listaAluno/")
    return render_to_response ("aluno/removeAluno.html", {'item':item}, context_instance=RequestContext(request))

@login_required
def ListaTurmasdoAluno(request, id):
    print "aluno" + id
    aluno = get_object_or_404 (Aluno, pk=id)
    matriculas = Matricula.objects.all().filter(nmAluno__id=id)
    turmas = []
    i = 0
    for obj in matriculas:
        turmas.append(obj.nmTurma)
        print turmas[i]
        i = i + 1
   
    # lista = Turma.objects.all().filter(pk__in=turmas)
    

    # lista = Matricula.objects.all().filter( nmAluno__icontains=aluno)
    # if request.method == "POST":
    #    aluno = request.POST['aluno']
    #    lista = Aluno.objects.all().filter( nmAluno__icontains=aluno)
    
    request.session['relatorio_aluno'] = lista
    return render_to_response ("turma/listaTurma.html", {'lista': lista}, context_instance=RequestContext(request)) 


def validacao(request_form):
    warning = True
    if request_form.POST['nmAluno'] == '':
        messages.add_message(request_form, messages.WARNING, 'Informe nome do aluno')
        warning = False
    return warning
