from django.contrib import admin
from .models import Proveedor
from .models import Fabricante
from .models import Capacidad
from .models import HistorialCompras
from .models import NasModelo
from .models import DiscoModelo

# Register your models here.
admin.site.register(Proveedor)
admin.site.register(Fabricante)
admin.site.register(Capacidad)
admin.site.register(HistorialCompras)
admin.site.register(NasModelo)
admin.site.register(DiscoModelo)