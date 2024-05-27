from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
# importar modelos
from .models import *
# menjar errores en ls db
from django.db import Error, transaction


# vista incial
def index(request):
    return render(request, "login.html")


# vista del admin
def admin(request):
    if request.user.is_authenticated:
        session_data = { "user": request.user, "rol": request.user.groups.get().name }
        return render(request, "administrador/index.html", session_data)
    else:
        mensaje = "Iniciar sesion"
        return render(request, "login.html", { "mensaje": mensaje })


# vista del empleado
def empledo(request):
    if request.user.is_authenticated:
        session_data = { "user": request.user, "rol": request.user.groups.get().name }
        return render(request, "empleado/index.html", session_data)
    else:
        mensaje = "Iniciar sesion"
        return render(request, "login.html", { "mensaje": mensaje })


# vista del tecnico
def tecnico(request):
    if request.user.is_authenticated:
        session_data = { "user": request.user, "rol": request.user.groups.get().name }
        return render(request, "tecnico/index.html", session_data)
    else:
        mensaje = "Iniciar sesion"
        return render(request, "login.html", { "mensaje": mensaje })


# incio de sesion
@csrf_exempt
def log_in(request):
    username = request.POST["user"]
    password = request.POST["password"]
    
    user = authenticate(username = username, password = password)
    
    if user is not None:
        # veridica quien se esta loggeando en la aplicacion
        auth.login(request, user)
        
        if user.groups.filter(name='Administrador').exists():
            return redirect('/administrador')
        elif user.groups.filter(name='Tecnico').exists():
            return redirect('/tecnico')
        else:
            return redirect('/empleado')
        
    # en caso de ingresar las credenciales incorrectas
    else:
        mensaje = "user or password is incorrect"
        return render(request, "login.html", { "mensaje": mensaje })
    
    

# vista solicitud
def solicitud_view(request):
    if request.user.is_authenticated:
        ambientes = Ambiente.objects.all()
        session_data = {
            "user": request.user,
            "rol": request.user.groups.get().name,
            "ambientes": ambientes
        }
        
        return render(request, "empleado/solicitud.html", session_data)
    else:
        mensaje = "iniciar sesion"
        return render(request, "login.html", { "mensaje": mensaje })



from random import randint
# registrando las solicitudes
def registro_solicitud(request):
    
    try:
        # valida que se guarde la informacon en ambas colecciones, no solamente en una
        with transaction.atomic():
            # guardando solicitud
            user = request.user
            descripcion = request.POST["descripcion"]
            id_ambiente = int(request.POST["id_ambiente"])
            ambiente = Ambiente.objects.get(pk=id_ambiente)
            solicitud = Solicitud(
                solicitudUsuario = user,
                solicitudAmbiente = ambiente,
                descripcion = descripcion
            )
            solicitud.save()
            
            # guardando caso
            consecutivo = randint(1,1000)
            codigo_caso = f"REQ {str(consecutivo).rjust(5, '0')}"
            caso_user = Usuario.objects.filter(groups__name__in=['Administrador']).first()
            caso = Caso(
                solicitudCaso = solicitud,
                codigo = codigo_caso,
                estado = 'Solicitada',
                tecnicoAsignado = caso_user
            )
            caso.save()

            return render(request, 'empleado/solicitud.html');        
    # en caso de que hay algun error
    except Error as error:
        transaction.rollback()
        print("Error al registrar la solicitud")
        print(error)
        mensaje = error;
        return render(request, 'empleado/solicitud.html', {"message": mensaje})