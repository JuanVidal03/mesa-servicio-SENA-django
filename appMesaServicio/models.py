from django.db import models
from django.contrib.auth.models import AbstractUser


# Ambientes de formacion
class Ambiente(models.Model):
    
    tipo_ambiente = [
        ('Formacion', 'Formacion'), ('Administrativo', 'Administrativo')
    ]
    
    nombre = models.CharField(max_length=100, unique=True)
    tipoAmbiente = models.CharField(choices=tipo_ambiente, max_length=50)
    
    def __str__(self)->str:
        return self.nombre


# usuarios, empleados, administrador
class Usuario(AbstractUser):
    
    tipo_usuario = [
        ('Admistrativo','Admistrativo'),
        ('Instructor','Instructor')
    ]
    
    tipoUsuario = models.CharField(max_length=50, choices=tipo_usuario)
    fotoUsuario = models.FileField(upload_to='fotos/', null=True, blank=True)
    fechaCracion = models.DateTimeField(auto_now_add=True)
    frechaActualizacion = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.first_name


# solicitud a mesa de ayuda
class Solicitud(models.Model):
    
    fechaInicioSolicitud = models.DateTimeField(auto_now_add=True)
    fechaFinalizacionSolicitud = models.DateTimeField(auto_now=True)
    descripcion = models.TextField(max_length=2000)
    solicitudUsuario = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    solicitudAmbiente = models.ForeignKey(Ambiente, on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return self.descripcion
    

# casos a solucionar en la mesa de ayuda
class Caso(models.Model):
    
    tipos_estado = [
        ('Solicitado', 'Solicitado'),
        ('Asignado', 'Asignado'),
        ('Finalizado', 'Finalizado')
    ]
    
    solicitudCaso = models.ForeignKey(Solicitud, on_delete=models.PROTECT)
    codigo = models.CharField(max_length=10, unique=True)
    tecnicoAsignado = models.ForeignKey(Usuario, on_delete=models.PROTECT)
    estado = models.CharField(choices=tipos_estado, max_length=30)
    
    def __str__(self)->str:
        return self.codigo

# tipos de problemas que se pueden solucionar
class TipoProcedimiento(models.Model):
    
    nombre = models.CharField(max_length=30, unique=True)
    descripcion = models.TextField(max_length=2000)
    
    def __str__(self) -> str:
        return self.nombre
    

# solucion de casos
class SolucionCaso(models.Model):
    
    tipo_solucion = [
        ('Parcial', 'Parcial'),
        ('Definitiva', 'Definitiva')
    ]
    
    caso = models.ForeignKey(Caso, on_delete=models.PROTECT,)
    procedimiento = models.TextField(max_length=2000)
    tipoSolucion = models.CharField(max_length=20, choices=tipo_solucion)
    fechaHoraCreacion = models.DateTimeField(auto_now_add=True,)
    fechaHoraActualizacion = models.DateTimeField(auto_now=True,)
    
    def __str__(self) -> str:
        return self.procedimiento


# solucion tipo caso procedimiento
class SolucionCasoTipoProcedimientos(models.Model):
    solSolucionCaso = models.ForeignKey(SolucionCaso, on_delete=models.PROTECT)
    solTipoProcedimiento = models.ForeignKey(TipoProcedimiento, on_delete=models.PROTECT)