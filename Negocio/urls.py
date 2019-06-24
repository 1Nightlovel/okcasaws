from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('recuperar/', views.recuperar, name='recuperar'),
    path('crearUsuario/', views.crearUsuario, name='crearUsuario'),
    path('crearTecnico/', views.crearTecnico, name='crearTecnico'),
    path('login_iniciar/', views.login_iniciar, name='login_iniciar'),
    path('cerrar_session/', views.cerrar_session, name='cerrar_session'),
    path('menu/', views.menu, name='menu'),
    path('agendar/', views.agendar, name='agendar'),
    path('historial/', views.historial, name='historial'),
    path('admin/', views.admin, name='admin'),
    path('tecnico/', views.tecnico, name='tecnico'),
    path('register_tecnico/', views.register_tecnico, name='registro_tecnico'),
    path('listado_tecnico/', views.listado_tecnico, name='listado_tecnico'),
    



    
    

]