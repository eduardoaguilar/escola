from django.shortcuts import render_to_response  , get_object_or_404
from django.http import HttpResponseRedirect
from models import Curso
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.template.context import RequestContext

nome_relatorio = "relatorio_curso"

@login_required
def listaCurso(request):
    lista = Curso.objects.all 
    if request.method == "POST":
        curso = request.POST['curso']
        lista = Curso.objects.all().filter(nmCurso__icontains=curso)
    #lista = lista.order_by('nmCurso')
    request.session['relatorio_curso'] = lista
    
    return render_to_response ("curso/listaCurso.html", {'lista': lista}, context_instance=RequestContext(request)) 
 
@login_required
def adicionaCurso (request):
    if request.method == "POST":
        f_curso = Curso(
                nmCurso=request.POST['nmCurso'],
                )
        f_curso.save()
        return HttpResponseRedirect ("/listaCurso/")
    return render_to_response ("curso/adicionaCurso.html", context_instance=RequestContext(request))  
 
@login_required
def itemCurso(request, nr_item):                   
    item = get_object_or_404 (Curso, pk=nr_item)   
    if request.method == "POST":
        f_curso = Curso(
                    id=item.id,
                    nmCurso=request.POST['nmCurso'])
        f_curso.save()
        return HttpResponseRedirect ("/itemCurso/" + str(nr_item) + "/")
    return render_to_response ('curso/itemCurso.html', {"curso":item}, context_instance=RequestContext(request))

@login_required
def removeCurso(request, nr_item):
    item = get_object_or_404 (Curso, pk=nr_item) 
    if request.method == "POST":
        item.delete() 
        messages.add_message(request, messages.WARNING, 'CURSO REMOVIDO')
        return HttpResponseRedirect("/listaCurso/")
    return render_to_response ("curso/removeCurso.html", {'item':item}, context_instance=RequestContext(request))

