from django.contrib import admin

# Register your models here.

from empresas.models import Empresa
admin.site.register(Empresa)

from empresas.models import Valoracion
admin.site.register(Valoracion)
