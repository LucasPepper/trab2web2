from django import forms

from .models import Aluno

from django.core.mail.message import EmailMessage

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = [
            'nome',
            'data_nascimento',
            'data_ingresso',
            'cpf',
            'rg',
            'email',
            'foto',
            'curso',
        ]