# _*_ encondig: utf-8 _*_


from django.shortcuts import render_to_response  , get_object_or_404 , render
from django.http import HttpResponseRedirect
from models import Aluno, Local, Curso, Turma, Matricula, Periodo
from forms import FormAluno,FormItemLocal, FormItemCurso , FormTurma, FormMatricula
from django.contrib import messages
from django.http.response import HttpResponseRedirect, HttpResponse
import datetime

from django.contrib.auth.decorators import login_required, user_passes_test,\
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
def inicio(request):
    return render(request, "inicio.html")


#####CONTROLE LOCAL
################################################################################
@login_required
def listaLocal(request):
    listaLocal_itens =  Local.objects.all 
    #listaLocal_itens = listaLocal_itens.order_by('nmLocal')
    return render_to_response ("local/listaLocal.html",{'lista': listaLocal_itens}, 
        context_instance=RequestContext(request)) # para funcionar o icone da lixeira. adciona a configuracao media_url

@login_required
def adicionaLocal (request):
    if request.method == "POST":
        f_local = Local( 
                nmLocal = request.POST['nmLocal'],
                )
        f_local.save()
        return HttpResponseRedirect ("/listaLocal/")
    return render_to_response ("local/adicionaLocal.html",context_instance=RequestContext(request))  # essa linha eh um mecansmo de proteao

@login_required
def itemLocal(request,nr_item):                   
    item = get_object_or_404 (Local, pk=nr_item )   
    if request.method == "POST":
        f_local = Local(
                    id = item.id,
                    nmLocal = request.POST['nmLocal'])
        f_local.save()
        return HttpResponseRedirect ("/itemLocal/"+str(nr_item)+"/")
    return render_to_response ('local/itemLocal.html',{"local":item}, context_instance=RequestContext(request))
            
@login_required
def removeLocal(request,nr_item):
    warning = True
    item = get_object_or_404 (Local, pk=nr_item) # todos os usuarios,usuario=request.user)
    if request.method =="POST":
        item.delete() 
        #return render_to_response("removido.html",{})
        messages.add_message(request, messages.WARNING,'LOCAL REMOVIDO')
        return HttpResponseRedirect("/listaLocal/")
    return render_to_response ("local/removeLocal.html", {'item':item},context_instance=RequestContext(request))
from django.shortcuts import render_to_response  , get_object_or_404 , render
from django.http import HttpResponseRedirect
from models import Aluno, Local, Curso, Turma, Matricula, Periodo
from django.contrib import messages
from django.http.response import HttpResponseRedirect, HttpResponse
import datetime
from django.contrib.auth.decorators import login_required, user_passes_test,\
    permission_required

from django.template.context import RequestContext
from datetime import timedelta

from django.template import RequestContext
from django.views.generic import ListView

nome_relatorio = "relatorio_curso"


@login_required
def listaCurso(request):
    listaCurso_itens =  Curso.objects.all 
    return render_to_response ("curso/listaCurso.html",{'lista': listaCurso_itens}, 
        context_instance=RequestContext(request)) 
 
@login_required
def adicionaCurso (request):
    if request.method == "POST":
        f_curso = Curso( 
                nmCurso = request.POST['nmCurso'],
                )
        f_curso.save()
        return HttpResponseRedirect ("/listaCurso/")
    return render_to_response ("curso/adicionaCurso.html",context_instance=RequestContext(request))  
 
@login_required
def itemCurso(request,nr_item):                   
    item = get_object_or_404 (Curso, pk=nr_item )   
    if request.method == "POST":
        f_curso = Curso(
                    id = item.id,
                    nmCurso = request.POST['nmCurso'])
        f_curso.save()
        return HttpResponseRedirect ("/itemCurso/"+str(nr_item)+"/")
    return render_to_response ('curso/itemCurso.html',{"curso":item}, context_instance=RequestContext(request))

@login_required
def removeCurso(request,nr_item):
    item = get_object_or_404 (Curso, pk=nr_item) 
    if request.method =="POST":
        item.delete() 
        messages.add_message(request, messages.WARNING,'CURSO REMOVIDO')
        return HttpResponseRedirect("/listaCurso/")
    return render_to_response ("curso/removeCurso.html", {'item':item},context_instance=RequestContext(request))


#### CONTROLE PERIODO

@login_required
def adicionaPeriodo (request):
    
    if request.method == "POST": 
        _periodo = request.POST['nmPeriodo'].replace('/','')
        if not _periodo:
            _periodo = None
        f_periodo = Periodo( 
                nmPeriodo = _periodo,
                )
        f_periodo.save()
        
        return HttpResponseRedirect ("/listaPeriodo/")
    return render_to_response ("periodo/adicionaPeriodo.html",context_instance=RequestContext(request))  

@login_required
def listaPeriodo(request):
    lista =  Periodo.objects.all
    return render_to_response ("periodo/listaPeriodo.html",{"lista": lista}, 
        context_instance=RequestContext(request)) 

def validacao(request_form):
    warning = True
    if request_form.POST['nmAluno'] == '':
        messages.add_message(request_form,messages.WARNING,'Informe nome do aluno')
        warning = False
    return warning