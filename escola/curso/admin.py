from models import Aluno 
from models import Curso
from models import Local
from models import Turma
from models import Matricula

from django.contrib import admin

#admin.site.register(Aluno)
admin.site.register(Curso)
admin.site.register(Local)
admin.site.register(Turma)
#admin.site.register(Matricula)
#admin.site.register(Professor)

class ItemAlunoAdmin(admin.ModelAdmin):
    fields = ('nmAluno','dtMatricula')#,'usuario','participa') # mostra todos esses campos nos detalhes
    list_display = ('nmAluno','dtMatricula')#,'usuario') # mostra somente esses campos na lista inicial
   
    #abaixo usado para gravar o usuario pois este nao aparece na tela. tem que pegar do 
    #variavel request.user e gravar no objeto que estah sendo manipulado
    def save_model(self,request,obj,form,change):
        obj.usuario = request.user
        obj.save()
    #para filtrar somente os dados do usuario que estah logado
    #def queryset(self,request):
    #    qs = super(ItemAlunoAdmin,self).queryset(request)  # retorna todos os registros da base
    #    return qs.filter(usuario=request.user) # filtra somente os dados do usuario logado
        
class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('nmTurma', 'nmAluno') 
    list_filter = ['nmTurma']
    search_field = ['nmAluno']

#class TurmaAdmin(admin.ModelAdmin):
#    fields = ('nmCurso','nmLocal') #,'participantes')
#    list_display = ('nmCurso','nmLocal')
   
admin.site.register(Matricula,MatriculaAdmin)
admin.site.register(Aluno,ItemAlunoAdmin)

