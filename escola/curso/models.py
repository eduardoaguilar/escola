from django.db import models
from django.contrib.auth.models import User
    
class Curso(models.Model):
    nmCurso      = models.CharField(max_length=40)
    def __unicode__(self):
        return self.nmCurso
    
class Local(models.Model):
    nmLocal = models.CharField(max_length=50)
    def __unicode__(self):
        return self.nmLocal

class Turma(models.Model):
    nmCurso = models.ForeignKey(Curso)
    nmLocal = models.ForeignKey(Local)
    dtPeriodo = models.CharField(max_length=20)
    class Meta:
        db_table = 'curso_turma'
    def __unicode__(self):
        return self.nmCurso,self.nmLocal,self.dtPeriodo

class Aluno(models.Model):  
    nmAluno      = models.CharField(max_length=60)
    dtMatricula  = models.DateField('matricula')
    #usuario      = models.ForeignKey(User)
    #participa    = models.ManyToManyField(Turma,related_name="turma_aluno") 
    def __unicode__(self):
        return self.nmAluno

class Matricula(models.Model):
    nmTurma = models.ForeignKey(Turma)
    nmAluno = models.ForeignKey(Aluno)
    class Meta:
        db_table = 'curso_matricula'
    

