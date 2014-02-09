from django import forms
from models import Aluno
from models import Local, Curso, Turma, Matricula

class FormAluno (forms.ModelForm):
    class Meta:
        model = Aluno 
        fields = ('nmAluno', 'dtMatricula')  
        
class FormItemLocal (forms.ModelForm):
    class Meta:
        model = Local
        
class FormItemCurso (forms.ModelForm):
    class Meta:
        model = Curso
       
class FormTurma (forms.ModelForm):
    class Meta:
        model = Turma
        fields = ('nmCurso','nmLocal','dtPeriodo')
        
class FormMatricula (forms.ModelForm):
    class Meta:
        model = Matricula
        fields = ('nmTurma','nmAluno')
        
       