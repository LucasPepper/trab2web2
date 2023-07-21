from django.shortcuts import render

from django.views import generic

from .models import Aluno, Matricula

from .forms import ContatoForm, RawAlunoForm, AlunoForm

from django.contrib import messages

# def raw_aluno_create_view(request):
#     form = RawAlunoForm(request.GET)
#     if request.method == "POST":
#         form = RawAlunoForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#         else:
#             print(form.errors)
#     context = {
#         "form": form
#     }
#     return render(request, "cadastro_aluno.html", context)

def aluno_create_view(request):
    form = AlunoForm(request.GET)
    if request.method == "POST":
        form = AlunoForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # Aluno.objects.create()
        else:
            print(form.errors)
    context = {
        "form": form
    }
    return render(request, "create.html", context)

def AlunosListView(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)

    queryset = Aluno.objects.all()
    queryset = queryset.order_by("nome")
    context = {
        "alunos_list": queryset
    }
    return render(request, "alunos_cadastrados.html", context)

class MatriculaDetailView(generic.DetailView): # matricula/ID_ALUNO
    template_name = 'matricula_detail.html'
    model = Matricula
    queryset = Matricula.objects.all()

def contact_view(request, *args, **kwargs):

    form = ContatoForm()
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():

            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            assunto = form.cleaned_data['assunto']
            mensagem = form.cleaned_data['mensagem']
            
            print('Mensagem Enviada')
            messages.success(request, 'E-mail enviado com sucesso')
            print(f'Nome: {nome}')
            print(f'E-mail: {email}')
            print(f'Assunto: {assunto}')
            print(f'Mensagem: {mensagem}')
            
        else:
            messages.error(request,'Erro ao enviar e-mail')

    return render(request, 'contact.html', {'form': form})