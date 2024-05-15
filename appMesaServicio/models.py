from django.db import models

"""
# roles de los usuario de la aplicacion
class Roles(models.Model):
    nombre = models.CharField(max_length=100)
"""

# Ambientes de formacion
class Ambiente(models.Model):
    
    tipo_ambiente = [
        ('Formacion', 'Formacion'), ('Administrativo', 'Administrativo')
    ]
    
    nombre = models.CharField(max_length=100, unique=True)
    tipoAmbiente = models.CharField(choices=tipo_ambiente, max_length=50)
    
    def __str__(self)->str:
        return self.nombre
    

"""
# empleados de mesa de servicio
class Empleado(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    cargo = models.CharField(max_length=100)
"""