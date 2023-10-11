from django.shortcuts import render, redirect
from .models import Usuario

def home(request):
    return render(request,'usuarios/home.html')

def admini(request):
    return render(request,"usuarios/admini.html")

def usuarios(request):
    usuarios = Usuario.objects.all()
    if request.method == 'POST':

        cpf = request.POST.get('cpf')

        if Usuario.objects.filter(cpf=cpf).exists(): # Para não cadastrar duas vezes do mesmo jeito
            return render(request, "usuarios/cpf_cadastrado.html")
           
        else:
            novo_usuario = Usuario()
            novo_usuario.nome = request.POST.get('nome')
            novo_usuario.idade = request.POST.get('idade')
            novo_usuario.cpf = request.POST.get('cpf')
            novo_usuario.save()

            return render(request, "usuarios/admini.html")

    return render(request,"usuarios/usuarios.html",{'usuarios':usuarios})

def index(request):
    total_usuarios = Usuario.objects.count()
    return render(request,"usuarios/index.html", {"total_usuarios":total_usuarios})

def excluir_usuario(request, usuario_id):
    usuario = Usuario.objects.get(pk=usuario_id)
    usuario.delete()
    return redirect('listagem_usuarios')