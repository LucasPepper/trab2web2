from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Aluno

from .forms import AlunoForm

from django.shortcuts import  render
from django.core.files.storage import FileSystemStorage

def aluno_create_view(request):
    if request.method == "POST":
        form = AlunoForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()

            # redirect to a new URL:
            return HttpResponseRedirect('/')
            
        else:
            print(form.errors)
        
    form = AlunoForm()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        "form": form,
        "num_visits": num_visits
    }
    return render(request, "cadastro_aluno.html", context)

def AlunosListView(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)

    queryset = Aluno.objects.all()
    queryset = queryset.order_by("nome")
    context = {
        "alunos_list": queryset
    }
    return render(request, "alunos_cadastrados.html", context)