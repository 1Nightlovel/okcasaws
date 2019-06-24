from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Usuario
from django.contrib.auth.models import User, Permission
from django.contrib.auth import authenticate,logout,login as auth_login
from django.contrib.auth.decorators import login_required,permission_required
from django.db.models import Q
# Create your views here.

def index(request):
    return render(request,'index.html', {})

def login(request):
    user = request.user
    if (user.is_anonymous):
        return render(request,'login.html',{})
    else:
        return render(request,'menu.html', {})
    

def register(request):
    return render(request,'register.html', {})

def register_tecnico(request):
    return render(request,'register-tecnico.html', {})

def recuperar(request):
    return render(request,'recuperar-contraseña.html',{})

def agendar(request):
    return render(request,'agendar.html',{})

def historial(request):
    return render(request,'historial.html',{})
    
@login_required(login_url='login')
def menu(request):
    user = request.user
    if user.has_perm('Negocio.is_cliente'):
        print("cliente log")
        return render(request,'menu.html', {})
    elif user.has_perm('Negocio.is_tecnico'):
        print("tecnico log")
        return render(request,'tecnico.html', {})
    elif user.has_perm('Negocio.is_administrador'):
        print("admin log")
        return render(request,'admin.html', {})
    elif user.is_anonymous:
        print("way4")
        return render(request,'login.html',{})
    else:
        return HttpResponse("<script>alert('no se que hacer')</script>")
        

        
@login_required(login_url='login')
def admin(request):
    user = request.user
    return render(request,'admin.html', {})

@login_required(login_url='login')
def tecnico(request):
    user = request.user
    return render(request,'tecnico.html', {})


def crearUsuario(request):

    rut = request.POST.get('rut','')
    nombre= request.POST.get('nombre','')
    apellido = request.POST.get('apellido','')
    email = request.POST.get('email','')
    telefono = request.POST.get('telefono',0)
    contrasenia = request.POST.get('contrasenia','')
    

    u = User.objects.create_user(username=email,password=contrasenia,first_name=nombre,last_name=apellido,email=email)
    usuario = Usuario(credenciales=u,rut=rut,nombre=nombre,apellido=apellido,email=email,telefono=telefono)
    u.save()
    usuario.save()
    permission = Permission.objects.get(name='is cliente')
    u.user_permissions.add(permission)
    return redirect('login')

@login_required(login_url='login')
def crearTecnico(request):

    rut = request.POST.get('rut','')
    nombre= request.POST.get('nombre','')
    apellido = request.POST.get('apellido','')
    email = request.POST.get('email','')
    telefono = request.POST.get('telefono',0)
    contrasenia = request.POST.get('contrasenia','')
    

    u = User.objects.create_user(username=email,password=contrasenia,first_name=nombre,last_name=apellido,email=email)
    usuario = Usuario(credenciales=u,rut=rut,nombre=nombre,apellido=apellido,email=email,telefono=telefono)
    u.save()
    usuario.save()
    permission = Permission.objects.get(name='is tecnico')
    u.user_permissions.add(permission)
    return redirect('menu')

def login_iniciar(request):

    username = request.POST.get('user','')
    contrasenia = request.POST.get('password','')
    user = authenticate(request,username=username,password=contrasenia)
    print(user)
    if user is not None:
        print("way1")
        auth_login(request, user)
        request.session['usuario'] = user.first_name+" "+user.last_name
        return redirect("menu")
    else:
        print("way2")
        return redirect("login")

@login_required(login_url='login')
def cerrar_session(request):
    del request.session['usuario']
    logout(request)
    return redirect('index')

def listado_tecnico(request):

    perm = Permission.objects.get(codename='is_administrador')  
    tecnicos = User.objects.filter(Q(groups__permissions=perm) | Q(user_permissions=perm))
    return render(request,'listadotecnicos.html', {'tecnicos':tecnicos})