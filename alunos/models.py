from django.db import models

from datetime import date

SITUACAO_ALUNO_CHOICES = (
    ('Aprovado', 'APROVADO'),
    ('Reprovado', 'REPROVADO'),
    ('Matriculado', 'MATRICULADO'),
    ('Dispensado', 'DISPENSADO'),
    ('Cancelado', 'CANCELADO'),
)

CURSO_CHOICES = (
    ('bsi', 'BSI'),
    ('tads', 'TADS'),
)

PERIODO_CHOICES = (
    ('2023/1', '2023/1'),
    ('2022/2', '2022/2'),
    ('2022/1', '2022/1'),
    ('2021/2', '2021/2'),
    ('2021/1', '2022/1'),
    ('2020/2', '2020/2'),
    ('2020/1', '2020/2'),
    ('2019/2', '2019/2'),
    ('2019/1', '2019/1'),
    ('2018/2', '2018/2'),
    ('2018/1', '2018/1'),
)

# Nome, Idade, Curso, Data de nascimento, CPF, RG, Data de ingresso na instituição, foto do aluno.
class Aluno(models.Model):
    nome = models.CharField('Nome', max_length=100)
    data_nascimento = models.DateField()
    # data_ingresso = models.DateField('Data de Ingresso', default="2023-02-01")
    foto = models.ImageField(upload_to='images/')
    cpf = models.CharField('CPF', max_length=11) # Somente números
    rg = models.CharField('RG', max_length=8) # Somente números 
    curso = models.CharField('Curso', max_length=15, choices=CURSO_CHOICES)
    email = models.EmailField('E-mail', max_length=50)

    def __str__(self):
        return self.nome
    
    def calcula_idade(self):
        today = date.today()
        idade = int(today.year) - int(self.data_nascimento.year) - ((int(today.month), int(today.day)) < (int(self.data_nascimento.month), int(self.data_nascimento.day)))
        return idade
    
    idade = calcula_idade
    
class Disciplina(models.Model):
    disciplina = models.CharField(max_length=20)

    def __str__(self):
        return self.disciplina
    
class Turma(models.Model):
    aluno = models.ManyToManyField(Aluno, related_name="turmas") # FK_ALUNO (Nº Matrícula)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT, blank=True, null=True, default=1) # FK_ALUNO (Nº Matrícula)
    nome = disciplina.get_attname
    periodo = models.CharField(choices=PERIODO_CHOICES, max_length=15) # PK

    def __str__(self):
        return f'{self.disciplina} '
    
class Matricula(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT) # FK_ALUNO (Nº Matrícula)
    turma = models.ForeignKey(Turma, on_delete=models.PROTECT) # FK_TURMA (Cód_Turma)
    nota = models.DecimalField('Nota', decimal_places=1, max_digits=3) # Cada aluno possui uma nota NAQUELA Turma
    situacao_aluno = models.CharField('Situação do Aluno', max_length=15, choices=SITUACAO_ALUNO_CHOICES) # Cada aluno possui uma situação NAQUELA Turma

    def __str__(self):
        return f'{self.aluno} {self.turma} {self.turma.periodo} {self.nota} {self.situacao_aluno}  '
    
class Contato(models.Model):
    nome = models.CharField('Nome', max_length=100)
    email = models.EmailField('E-mail', max_length=50)
    texto = models.CharField(max_length=120)