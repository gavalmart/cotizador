from django.db import models

# Create your models here.

class Proveedor(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    activo = models.BooleanField(null=False, default=True)
    actualizacionUsuario = models.IntegerField(null=True, blank=True)
    creacionFechaHora = models.DateTimeField(null=True, auto_now_add=True)
    actualizacionFechaHora = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return self.nombre
    

class Fabricante(models.Model):
    nombre = models.CharField(max_length=30, null=False)
    activo = models.BooleanField(null=False, default=True)
    actualizacionUsuario = models.IntegerField(null=True, blank=True)
    creacionFechaHora = models.DateTimeField(null=True, auto_now_add=True)
    actualizacionFechaHora = models.DateTimeField(null=True, auto_now=True)

    def __str__(self):
        return self.nombre
    

class Capacidad(models.Model):
    UNIDAD_MEDIDA = (
        ('MB', 'MB'),
        ('GB', 'GB'),
        ('TB', 'TB'),
        ('PB', 'PB'),
    )

    valor = models.IntegerField(null=False, default=0)
    unidadMedida = models.CharField(max_length=2, null=False, default='TB', choices=UNIDAD_MEDIDA)
    activo = models.BooleanField(null=False, default=True)
    actualizacionUsuario = models.IntegerField(null=True, blank=True)
    creacionFechaHora = models.DateTimeField(null=True, auto_now_add=True)
    actualizacionFechaHora = models.DateTimeField(null=True, auto_now=True)

    def __str__(self) -> str:
        return f'{self.valor} - {self.unidadMedida}'

class HistorialCompras(models.Model):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.deletion.SET_NULL, null=True)
    fechaCompra = models.DateField(null=True)
    codigo = models.CharField(max_length=60, null=False)
    activo = models.BooleanField(null=False, default=True)
    actualizacionUsuario = models.IntegerField(null=True, blank=True)
    creacionFechaHora = models.DateTimeField(null=True, auto_now_add=True)
    actualizacionFechaHora = models.DateTimeField(null=True, auto_now=True)

    def __str__(self) -> str:
        return self.codigo
    
    # def mostrarProveedorNombre(self) -> str:
    #     proveedor_actual = self.proveedor.nombre
        
    #     if proveedor_actual:
    #         return proveedor_actual
    #     else:
    #         return "empty"
    

class NasModelo(models.Model):
    GARANTIA_PERIODOS = ((1, 1),
                        (3, 3),
                         (5, 5),)
    modelo = models.CharField(max_length = 12, null=False, blank=False)
    anioLanzamiento = models.IntegerField(null=True, verbose_name='Año Lanzamiento')
    fabricante = models.ForeignKey(Fabricante, on_delete=models.deletion.SET_NULL, null=True)
    garantiaAnios = models.IntegerField(null=False, default= 1, choices=GARANTIA_PERIODOS, verbose_name='Años de Garantía')
    cantidadBahiasInternas = models.IntegerField(null=False, blank=True, default=1, verbose_name='Número Bahías Internas')
    cantidadUnidadesExpansion = models.IntegerField(null=True, blank=True, verbose_name='Cantidad Unidades de Expanasión')
    maxCantDiscosUnidadExpansion = models.IntegerField(null=True, blank=True, verbose_name='Discos por Unidad Expansión')
    ramIncluidaGB = models.IntegerField(null=True, blank=True, verbose_name='RAM Incluída (GB)')
    ramMax = models.IntegerField(null=True, blank=True, verbose_name='RAM Máxima (GB)')
    ramSlots = models.IntegerField(null=True, verbose_name='Ranuras para RAM')
    cantidadNics1Gb = models.IntegerField(null=True, blank=True, verbose_name='Adaptadores Red de 1 Gbps')
    cantidadNics10Gb = models.IntegerField(null=True, blank=True, verbose_name='Adaptadores Red de 10 Gbps')
    cantidadBahiasPci = models.IntegerField(null=True, blank=True, verbose_name='Ranuras PCI Express')
    esRackeable = models.BooleanField(null=False, default=False, verbose_name="Unidad de Rack")
    tieneFuentePoderRedundante = models.BooleanField(null=False, default=False, verbose_name="Unidad con fuente de poder redundante")
    activo = models.BooleanField(null=False, default=True)
    actualizacionUsuario = models.IntegerField(null=True, blank=True)
    creacionFechaHora = models.DateTimeField(null=True, auto_now_add=True)
    actualizacionFechaHora = models.DateTimeField(null=True, auto_now=True)

    def __str__(self) -> str:
        return self.modelo
    

class DiscoModelo(models.Model):
    GARANTIA_PERIODOS = ((1, 1),
                         (3, 3),
                         (5, 5),)
    modeloCorto = models.CharField(max_length=20, null=False, verbose_name='Modelo Comercial')
    modeloLargo = models.CharField(max_length=40, null=True, blank=True, verbose_name='Código del Modelo')
    descripcion = models.CharField(max_length=200, null=False, blank=False, verbose_name='Descripción')
    fabricante = models.ForeignKey(Fabricante, on_delete=models.deletion.SET_NULL, null=True)
    capacidad = models.ForeignKey(Capacidad, on_delete=models.deletion.SET_NULL, null=True)
    esSSD = models.BooleanField(null=False, default=False, verbose_name='Es SSD?')
    garantiaAnios = models.IntegerField(null=False, default=1, choices=GARANTIA_PERIODOS, verbose_name='Años de Garantía')
    rpms = models.IntegerField(null=True, verbose_name='RPMs')
    cacheEnMB = models.IntegerField(null=False, verbose_name='Cache en MB')
    activo = models.BooleanField(null=False, default=True)
    actualizacionUsuario = models.IntegerField(null=True, blank=True)
    creacionFechaHora = models.DateTimeField(null=True, auto_now_add=True)
    actualizacionFechaHora = models.DateTimeField(null=True, auto_now=True)


    def __str__(self) -> str:
        return self.modeloCorto
    