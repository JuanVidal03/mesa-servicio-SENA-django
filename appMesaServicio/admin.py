from django.contrib import admin

# importar los modelos
from .models import Ambiente

# permitir que el usuario acceda a los modelos 
admin.site.register(Ambiente)