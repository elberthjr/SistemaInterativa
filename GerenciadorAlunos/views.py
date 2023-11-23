from django.shortcuts import render, redirect
from GerenciadorAlunos.forms import AlunosForm
from GerenciadorAlunos.models import Alunos
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    return render(request, 'index.html')

def listaAlunos(request):
    data = {}
    busca_aluno = request.GET.get('busca_aluno')
    if busca_aluno:
        data['db'] = Alunos.objects.filter(nome__icontains=busca_aluno)
    else:
        data['db'] = Alunos.objects.all()

    # data['db'] = Alunos.objects.all()
    # all = Alunos.objects.all()
    # paginator = Paginator(all, 20)
    # pages = request.GET.get('page')
    # data['db'] = paginator.get_page(pages)
    return render(request, 'listaAlunos.html', data)

def addAluno(request):
    data = {}
    data['form'] = AlunosForm()
    return render(request, 'addAluno.html', data)

def createAluno(request):
    form = AlunosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listaAlunos')

def visualizarAluno(request, pk):
    data = {}
    data['db'] = Alunos.objects.get(pk=pk)
    return render(request, 'visualizarAluno.html', data)


def editarAluno(request, pk):
    data = {}
    data['db'] = Alunos.objects.get(pk=pk)
    data['form'] = AlunosForm(instance=data['db'])
    return render(request, 'addAluno.html', data)


def attAluno(request, pk):
    data = {}
    data['db'] = Alunos.objects.get(pk=pk)
    form = AlunosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('listaAlunos')


def apagarAluno(request, pk):
    db = Alunos.objects.get(pk=pk)
    db.delete()
    return redirect('home')