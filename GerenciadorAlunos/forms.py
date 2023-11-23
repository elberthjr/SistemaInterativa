from django.forms import ModelForm
from GerenciadorAlunos.models import Alunos

class AlunosForm(ModelForm):
    class Meta:
        model = Alunos
        fields = ['nome', 'curso', 'dataInicio', 'presencas', 'aulasRestantes']