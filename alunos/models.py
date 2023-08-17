from django.db import models

from datetime import date

CURSO_CHOICES = (
    ('BSI', 'BSI'),
    ('TADS', 'TADS'),
)

# Nome, Idade, Curso, Data de nascimento, CPF, RG, Data de ingresso na instituição, foto do aluno.
class Aluno(models.Model):
    nome = models.CharField('Nome', max_length=100, default="Test")
    data_nascimento = models.DateField(default="01/01/2000")
    data_ingresso = models.DateField('Data de Ingresso', default="2023-02-01")
    foto = models.ImageField(upload_to='alunos/static/images')
    cpf = models.CharField('CPF', max_length=11, default=111) 
    rg = models.CharField('RG', max_length=8, default=222) 
    curso = models.CharField('Curso', max_length=15, choices=CURSO_CHOICES, default='BSI')
    email = models.EmailField('E-mail', max_length=50, default='test@test.com')
    test = models.CharField(max_length=50)

    def __str__(self):
        return self.nome
    
    def calcula_idade(self):
        today = date.today()
        idade = int(today.year) - int(self.data_nascimento.year) - ((int(today.month), int(today.day)) < (int(self.data_nascimento.month), int(self.data_nascimento.day)))
        return idade
    
    idade = calcula_idade
