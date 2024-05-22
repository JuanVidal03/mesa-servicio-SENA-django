from django.contrib import admin

# importar los modelos
from .models import Ambiente, Usuario, TipoProcedimiento

# permitir que el usuario acceda a los modelos 
admin.site.register(Ambiente)
admin.site.register(Usuario)
admin.site.register(TipoProcedimiento)