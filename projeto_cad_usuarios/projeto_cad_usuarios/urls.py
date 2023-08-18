

from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    #aqui esta a minha rota para visualizar na pagina web
    path('',views.home,name='home'),

    path('usuarios/',views.usuarios,name='listagem_usuarios')
]
