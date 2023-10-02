from django.shortcuts import render
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')

def admini(request):
    return render(request,"usuarios/admini.html")

def usuarios(request):
    # Salvar os dados da tela para o banco de dados.
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.cpf = request.POST.get('cpf')
    novo_usuario.save()

    # Exibir todos os usuarios jpa cadastrados em uma nova página
    usuarios = {
        'usuarios': Usuario.objects.all()
    }
    
    # Retornar os dados para a página de listagem de usuarios
    return render(request,"usuarios/usuarios.html",usuarios)

