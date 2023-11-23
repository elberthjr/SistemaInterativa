"""
URL configuration for SistemaInterativa project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from GerenciadorAlunos.views import home, addAluno, listaAlunos, createAluno, visualizarAluno, editarAluno, attAluno, apagarAluno

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('addAluno/', addAluno, name='addAluno'),
    path('listaAlunos/', listaAlunos, name='listaAlunos'),
    path('createAluno/', createAluno, name='createAluno'),
    path('visualizarAluno/<int:pk>/', visualizarAluno, name='visualizarAluno'),
    path('editarAluno/<int:pk>/', editarAluno, name='editarAluno'),
    path('attAluno/<int:pk>/', attAluno, name='attAluno'),
    path('apagarAluno/<int:pk>/', apagarAluno, name='apagarAluno'),
]
