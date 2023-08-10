from django import forms

from .models import Aluno, Turma

from django.core.mail.message import EmailMessage

# Raw
class RawAlunoForm(forms.Form):

    nome = forms.CharField(label='Nome', max_length=100)
    data_nascimento = forms.DateField(label='Data de Nascimento')
    cpf = forms.CharField(label='CPF') # Somente números
    rg = forms.CharField(label='RG') # Somente números 
    email = forms.EmailField(label='E-mail')
    foto = forms.ImageField()
    curso = forms.CharField(label='Curso')
    data_ingresso = forms.DateField(label='Data de Ingresso no Curso')

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

class ContatoForm(forms.Form):

    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=100)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

def send_mail(self):
    nome = self.cleaned_data['nome']
    email = self.cleaned_data['email']
    assunto = self.cleaned_data['assunto']
    mensagem = self.cleaned_data['mensagem']

    conteudo = f'Nome: {nome}\nE-mail: {email}\nAssunto: {assunto}\nMensagem: {mensagem}'
    mail = EmailMessage (
        subject='E-mail enviado pelo sistema Django',
        body = conteudo,
        from_email='pimentalucas@hotmail.com',
        to=['pimentalucas@hotmail.com', ],
        headers={'Reply.To':email},
    )
    print('send_mail')
    mail.send()