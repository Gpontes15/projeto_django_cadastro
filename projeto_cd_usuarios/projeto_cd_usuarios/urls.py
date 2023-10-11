
from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    # rota, view responsavel, nome de referencia
    # usuarios.com
    path('index/',views.home,name='home'),
    # usuarios.com/usuarios
    path('usuarios/',views.usuarios,name='listagem_usuarios'),
    # Deletar e editar usuarios
    path('admini/',views.admini,name='admini'),
    # pagina principal
    path('',views.index,name='index'),
    # Excluir usuario
    path('excluir/<int:usuario_id>/', views.excluir_usuario, name='excluir_usuario'),

]
