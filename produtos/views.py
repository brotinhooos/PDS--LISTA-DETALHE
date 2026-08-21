from django.shortcuts import render

from . import models

# Create your views here.
def listagem(request):
    alunos = models.aluno.objects.all()
    return render(request, 'produtos/listagem.html', {'alunos': alunos})

def detalhes(request, id):
    aluno = models.aluno.objects.get(id=id)
    return render(request, 'produtos/listagem.html', {'aluno': aluno})
    
