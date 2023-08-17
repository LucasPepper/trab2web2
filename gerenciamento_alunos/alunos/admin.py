from django.contrib import admin
from .models import Aluno, Turma, Matricula, Disciplina

# Register your models here.

class MatriculaAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'disciplina', 'periodoIngresso', 'nota', 'situacao')

admin.site.register(Aluno)
admin.site.register(Turma)
admin.site.register(Disciplina)
admin.site.register(Matricula)