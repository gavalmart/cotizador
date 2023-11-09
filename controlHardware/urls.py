"""cotizador URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('test/', views.test),
    path('test2/', views.test2),
    path('proveedores/', views.listarProveedores, name='listar_proveedores'),
    path('proveedores/agregar', views.agregarProveedor, name='agregar_proveedor'),
    path('proveedores/<str:id>', views.actualizarProveedor, name='actualizar_proveedor'),
    path('proveedores/eliminar/<str:id>', views.eliminarProveedor, name='eliminar_proveedor'),

    path('fabricantes/', views.listarFabricantes, name='listar_fabricantes'),
    path('fabricantes/agregar', views.agregarFabricante, name='agregar_fabricante'),
    path('fabricantes/<str:id>', views.actualizarFabricante, name='actualizar_fabricante'),
    path('fabricantes/eliminar/<str:id>', views.eliminarFabricante, name='eliminar_fabricante'),

    path('capacidades/', views.listarCapacidad, name='listar_capacidad'),
    path('capacidades/agregar', views.agregarCapacidad, name='agregar_capacidad'),
    path('capacidades/<str:id>', views.actualizarCapacidad, name='actualizar_capacidad'),
    path('capacidades/eliminar/<str:id>', views.eliminarCapacidad, name='eliminar_capacidad'),

    path('historialCompras/', views.listarHistorialCompras, name='listar_historialCompras'),
    path('historialCompras/agregar', views.agregarHistorialCompras, name='agregar_historialCompras'),
    path('historialCompras/<str:id>', views.actualizarHistorialCompras, name='actualizar_historialCompras'),
    path('historialCompras/eliminar/<str:id>', views.eliminarHistorialCompras, name='eliminar_historialCompras'),

    path('modelosDiscos/', views.listaDiscoModelo, name='listar_modeloDisco'),
    path('modelosDiscos/agregar', views.agregarDiscoModelo, name='agregar_modeloDisco'),
    path('modelosDiscos/<str:id>', views.actualizarDiscoModelo, name='actualizar_modeloDisco'),
    path('modelosDiscos/eliminar/<str:id>', views.eliminarDiscoModelo, name='eliminar_modeloDisco'),

    path('modelosNas/', views.listaNasModelo, name='listar_modeloNas'),
    path('modelosNas/agregar', views.agregarNasModelo, name='agregar_modeloNas'),
    path('modelosNas/<str:id>', views.actualizarNasModelo, name='actualizar_modeloNas'),
    path('modelosNas/eliminar/<str:id>', views.eliminarNasModelo, name='eliminar_modeloNas'),
]
