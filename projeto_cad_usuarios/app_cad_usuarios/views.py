from django.shortcuts import render
from .models import Usuario
# Create your views here.
# Crie suas visualizações aqui

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    #Salvar os dados da tela para o banco de dados
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.idade = request.POST.get('idade')
    novo_usuario.cpf = request.POST.get('cpf')
    novo_usuario.endereco = request.POST.get('endereço')
    novo_usuario.save()

    # Exibir todos os usuarios já cadastrado em uma nova página

    usuarios = {
        'usuarios': Usuario.objects.all()
    }

    #Retornar os dados para a pagina de listagem de usuários

    return render(request,'usuarios/usuarios.html',usuarios)