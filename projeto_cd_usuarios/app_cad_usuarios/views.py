from django.shortcuts import render, redirect
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')

def admini(request):
    return render(request,"usuarios/admini.html")

def usuarios(request):
    usuarios = Usuario.objects.all()

    if request.method == 'POST':
        novo_usuario = Usuario()
        novo_usuario.nome = request.POST.get('nome')
        novo_usuario.idade = request.POST.get('idade')
        novo_usuario.cpf = request.POST.get('cpf')
        novo_usuario.save()

        return render(request, "usuarios/admini.html")

    return render(request,"usuarios/usuarios.html",{'usuarios':usuarios})

def index(request):
    return render(request,"usuarios/index.html")

def excluir_usuario(request, usuario_id):
    usuario = Usuario.objects.get(pk=usuario_id)
    usuario.delete()
    return redirect('listagem_usuarios')