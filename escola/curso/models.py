from django.db import models
from django.contrib.auth.models import User
    
class Curso(models.Model):
    id = models.AutoField(primary_key=True)
    nmCurso= models.CharField(max_length=40)
    def __unicode__(self):
        return self.nmCurso
    class Meta:
        db_table = 'tbcurso'
    
    
class Local(models.Model):
    id = models.AutoField(primary_key=True)
    nmLocal = models.CharField(max_length=50)
    def __unicode__(self):
        return self.nmLocal
    class Meta:
        db_table = 'tblocal'
        
class Periodo(models.Model):
    id = models.AutoField(primary_key=True)
    nmPeriodo = models.CharField(max_length=5)
    def __unicode__(self):
        return self.nmPeriodo
    class Meta:
        db_table = 'tbperiodo'
        ordering = ['nmPeriodo']
       
class Turma(models.Model):
    id = models.AutoField(primary_key=True)
    nmCurso = models.ForeignKey(Curso)
    nmLocal = models.ForeignKey(Local)
    nmPeriodo = models.ForeignKey(Periodo)
    class Meta:
        db_table = 'tbturma'
        
    def __unicode__(self):
        return self.nmCurso,self.nmLocal,self.nmPeriodo

class Aluno(models.Model):  
    id = models.AutoField(primary_key=True)
    nmAluno      = models.CharField(max_length=60)
    dtMatricula  = models.DateField(null=True, blank=True)
    class Meta:
        db_table = 'tbaluno'
    
    #usuario      = models.ForeignKey(User)
    #participa    = models.ManyToManyField(Turma,related_name="turma_aluno") 
    def __unicode__(self):
        return self.nmAluno

class Matricula(models.Model):
    id = models.AutoField(primary_key=True)
    nmTurma = models.ForeignKey(Turma)
    nmAluno = models.ForeignKey(Aluno)
    class Meta:
        db_table = 'tbmatricula'
        ordering = ['nmTurma']

    

