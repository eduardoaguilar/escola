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
from django.contrib import messages
from django.http.response import HttpResponse
import datetime
from datetime import timedelta

from django.template import RequestContext
from django.views.generic import ListView

nome_relatorio = "relatorio_aluno"

@login_required
def inicio(request):
    return render(request, "index.html")

#####CONTROLE ALUNOS
@login_required
def listaAluno(request):
    if request.method == "POST":
        aluno = request.POST['aluno']
        lista = Aluno.objects.all().filter( nmAluno__icontains=aluno)
    else:
        lista =  Aluno.objects.all()
    request.session['relatorio_aluno'] = lista
    return render_to_response ("aluno/listaAluno.html",{'lista': lista},context_instance=RequestContext(request)) 
@login_required
def adicionaAluno (request):
    if request.method == "POST":
        f_aluno = Aluno( 
                nmAluno = request.POST['nmAluno'],
                dtMatricula = datetime.datetime.now(),
                )
        f_aluno.save()
        
        return HttpResponseRedirect ("/listaAluno/")
    return render_to_response ("aluno/adicionaAluno.html",context_instance=RequestContext(request))  
@login_required
def itemAluno(request,nr_item):                   
    item = get_object_or_404 (Aluno, pk=nr_item )   
    if request.method == "POST":
        f_aluno = Aluno(
                    id = item.id,
                    nmAluno = request.POST['nmAluno'],
                    dtMatricula = item.dtMatricula ,)
        f_aluno.save()
        return HttpResponseRedirect ("/itemAluno/"+str(nr_item)+"/")
    return render_to_response ('aluno/itemAluno.html',{"aluno":item}, context_instance=RequestContext(request))
            
@login_required
def removeAluno(request,nr_item):
    warning = True
    item = get_object_or_404 (Aluno, pk=nr_item) 
    if request.method =="POST":
        item.delete() 
        messages.add_message(request, messages.WARNING,'ALUNO REMOVIDO')
        return HttpResponseRedirect("/listaAluno/")
    return render_to_response ("aluno/removeAluno.html", {'item':item},context_instance=RequestContext(request))

@login_required
def listaTurmasdeAluno(request,nr_item):
    if request.method == "POST":
        aluno = request.POST['aluno']
        lista = Aluno.objects.all().filter( nmAluno__icontains=aluno)
    else:
        lista =  Aluno.objects.all()
        
    request.session['relatorio_aluno'] = lista
    return render_to_response ("aluno/listaAluno.html",{'lista': lista},context_instance=RequestContext(request)) 


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

#####CONTROLE CURSO
################################################################################
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

################################################################################ 
#####                          CONTROLE TURMA                      #############
################################################################################
@login_required
def listaTurma(request):
    listaTurma_itens =  Turma.objects.all 
    #lista_itens =  Aluno.objects.filter(usuario=request.user) # soh mostra os registros do usuario q esta logado
    return render_to_response ("turma/listaTurma.html",{'listaTurma_itens': listaTurma_itens}, 
        context_instance=RequestContext(request)) # para funcionar o icone da lixeira. adciona a configuracao media_url
@login_required
def adicionaTurma (request):
    curso = Curso.objects.all()
    local = Local.objects.all()
    periodo = Periodo.objects.all()
    if request.method == "POST":
        form = FormTurma (request.POST)
        if form.is_valid ():
            form.save()
            return HttpResponseRedirect("/listaTurma/")
    else:
        form = FormTurma()  
    return render_to_response ('turma/adicionaTurma.html',{"form":form,"curso":curso,"local":local,"periodo":periodo},context_instance=RequestContext(request))  # essa linha eh um mecansmo de proteao

@login_required
def itemTurma(request,nr_item): 
    curso = Curso.objects.all()
    local = Local.objects.all()
    item = get_object_or_404 (Turma, pk=nr_item )   
    if request.method == "POST":
        form = FormTurma (request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/itemTurma/"+str(nr_item)+"/")
        else:
            messages.add_message(request, messages.WARNING,'ERRO NA EDICAO')

    else:
        form = FormTurma(instance=item)
    return render_to_response ("turma/itemTurma.html", {'form':form, "curso":curso,"local":local},context_instance=RequestContext(request))
    
@login_required
def removeTurma(request,nr_item):
    item = get_object_or_404 (Turma, pk=nr_item) 
    if request.method =="POST":
        item.delete() 
        messages.add_message(request, messages.WARNING,'TURMA REMOVIDA')
        return HttpResponseRedirect("/listaTurma/")
    return render_to_response ("turma/removeTurma.html", {'item':item},context_instance=RequestContext(request))

################################################################################
#####                          CONTROLE MATRICULA
################################################################################
@login_required
def listaMatricula(request):
    lista =  Matricula.objects.all
    return render_to_response ("matricula/listaMatricula.html",{"lista": lista}, 
        context_instance=RequestContext(request)) 
    
@login_required
def adicionaMatricula (request):
    turma = Turma.objects.all()
    aluno = Aluno.objects.all()
    if request.method == "POST":
        form = FormMatricula (request.POST)
        if form.is_valid ():
            form.save()
            return HttpResponseRedirect("/listaMatricula/")
    else:
        form = FormMatricula()  
    return render_to_response ('matricula/adicionaMatricula.html',{"form":form,"turma":turma,"aluno":aluno},context_instance=RequestContext(request))  

@login_required
def itemMatricula(request,nr_item): 
    turma = Turma.objects.all()
    aluno = Aluno.objects.all()
    item = get_object_or_404 (Matricula, pk=nr_item )   
    if request.method == "POST":
        form = FormMatricula (request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/itemMatricula/"+str(nr_item)+"/")
        else:
            messages.add_message(request, messages.WARNING,'ERRO NA EDICAO')
    else:
        form = FormMatricula(instance=item)
    return render_to_response ('matricula/itemMatricula.html', {"form":form, "turma":turma,"aluno":aluno},context_instance=RequestContext(request))
    
@login_required
def removeMatricula(request,nr_item):
    item = get_object_or_404 (Matricula, pk=nr_item) 
    if request.method =="POST":
        item.delete() 
        messages.add_message(request, messages.WARNING,'MATRICULA REMOVIDA')
        return HttpResponseRedirect("/listaMatricula/")
    return render_to_response ("matricula/removeMatricula.html", {'item':item},context_instance=RequestContext(request))


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

