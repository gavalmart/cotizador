from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from .forms import ProveedorForm, FabricanteForm, CapacidadForm, HistorialComprasForm, NasModeloForm, DiscoModeloForm
from .models import Proveedor, Fabricante, Capacidad
from .models import HistorialCompras
from .models import NasModelo, DiscoModelo

# Create your views here.
def inicio(request):
    #return HttpResponse('inicio')
    return render(request, 'base.html')

def test(request):
    return HttpResponse('test')

def test2(request):
    return render(request, 'test.html')

# def AgregarProveedor(request):
#     proveedores = Proveedor.objects.all()

    #forma = ProveedorForm()
    
    
# doing the form manually, just with forms not ModelForm  
 
    # forma = ProveedorForm2()
    
    # if request.method == 'POST':
    #     forma = ProveedorForm2(request.POST)
    #     if forma.is_valid() :
    #         nombre = forma.cleaned_data['nombre']
    #         provedor = Proveedor.objects.create(nombre=nombre, activo = forma.cleaned_data['activo'])
    #         provedor.save()

    #         return HttpResponse(f'Proveedor creado con exito: {nombre}')

    # context = {'forma': forma.as_p, 'titulo': 'Agregar Proveedor'}

    # return render(request, 'proveedor_form.html', context)

# proveedores

def listarProveedores(request):
    proveedores = Proveedor.objects.all()
    context = {'titutlo': 'Listado de Proveedores', 'proveedores': proveedores}
    return render(request, 'proveedores/prov_listar.html', context)


def agregarProveedor(request):
    forma = ProveedorForm()
    context = {'titulo': 'Agregar Proveedor', 'forma': forma.as_p}
    if request.method == 'POST':
        forma = ProveedorForm(request.POST)
        if forma.is_valid():
            forma.save()
            return redirect ('listar_proveedores')

    return render(request, 'proveedores/prov_form.html', context)


def actualizarProveedor(request, id):
    # proveedor = Proveedor.objects.get(id=id)
    proveedor = get_object_or_404(Proveedor,id=id)
    forma = ProveedorForm(instance=proveedor)

    if request.method == 'POST':
        forma = ProveedorForm(request.POST, instance=proveedor)
        if forma.is_valid():
            forma.save()
            return redirect('listar_proveedores')

    context = {'titulo': 'Modificar Proveedor', 'forma': forma.as_p}
    return render(request, 'proveedores/prov_form.html', context)


def eliminarProveedor(request, id):
    proveedor = get_object_or_404(Proveedor, id=id)
    proveedor.delete()
    return redirect ('listar_proveedores')


# fabricantes

def listarFabricantes(request):
    fabricantes = Fabricante.objects.all()
    context = {'fabricantes':fabricantes}

    return render(request, 'fabricantes/fab_listar.html', context)


def agregarFabricante(request):
    titulo = 'Agregar Fabricante'
    forma = FabricanteForm()

    if request.method == 'POST':
        form = FabricanteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_fabricantes')

    context = {'titulo': titulo, 'forma': forma,}
    return render(request, 'fabricantes/fab_form.html', context)


def actualizarFabricante(request, id):
    titulo = 'Agregar Fabricante'
    fabricante = get_object_or_404(Fabricante, id=id)
    forma = FabricanteForm(instance=fabricante)

    if request.method == 'POST':
        forma  = FabricanteForm(request.POST, instance=fabricante)
        if forma.is_valid():
            forma.save()
            return redirect('listar_fabricantes')

    context = {'titulo': titulo, 'forma': forma}  
    return render(request, 'fabricantes/fab_form.html', context)


def eliminarFabricante(request, id):
    fabricante = get_object_or_404(Fabricante, id=id)
    fabricante.delete()
    return redirect('listar_fabricantes')


def listarCapacidad(request):
    capacidades = Capacidad.objects.all()
    context = {'capacidades': capacidades,}

    return render(request, 'capacidades/cap_listar.html', context)


def agregarCapacidad(request):
    forma = CapacidadForm()
    titulo = 'Agregar Capacidad de HDDs'

    if request.method == 'POST':
        forma = CapacidadForm(request.POST)
        if forma.is_valid():
            forma.save()
            return redirect('listar_capacidad')
    
    context = {'titulo': titulo, 'forma': forma}
    return render(request, 'capacidades/cap_form.html', context)



def actualizarCapacidad(request, id):
    capacidad = get_object_or_404(Capacidad, id = id)
    titulo = 'Modificar Capacidad de HDDs'
    forma = CapacidadForm(instance=capacidad)

    context = {'titulo': titulo, 'forma': forma}

    if request.method == 'POST':
        forma = CapacidadForm(request.POST, instance=capacidad)
        if forma.is_valid():
            forma.save()
            return redirect('listar_capacidad')

    return render(request, 'capacidades/cap_form.html', context)



def eliminarCapacidad(request, id):
    capacidad = get_object_or_404(Capacidad, id = id)
    capacidad.delete()

    return redirect('listar_capacidad')


def listarHistorialCompras(request):
    compras = HistorialCompras.objects.all()
    context = {'compras': compras}

    return render(request, 'historialCompras/comp_listar.html', context)


def agregarHistorialCompras(request):
    titulo = "Agregar registro de compra"

    if request.POST:
        forma = HistorialComprasForm(request.POST)
        if forma.is_valid():
            forma.save()
            return redirect('listar_historialCompras')
    else:
        forma = HistorialComprasForm()

    context = {'titulo': titulo, 'forma': forma}
    return render(request, 'historialCompras/comp_form.html', context)


def actualizarHistorialCompras(request, id):
    titulo = "Actualizar registro de compra"
    compra = get_object_or_404(HistorialCompras, id = id)

    if request.POST:
        forma = HistorialComprasForm(request.POST, instance=compra)
        if forma.is_valid():
            forma.save()
            return redirect('listar_historialCompras')
    else:
        forma = HistorialComprasForm(instance=compra)

    context = {'titulo': titulo, 'forma': forma}
    return render(request, 'historialCompras/comp_form.html', context)


def eliminarHistorialCompras(request, id):
    compra =  get_object_or_404(HistorialCompras, id = id)

    compra.delete()
    return redirect('listar_historialCompras')


def listaNasModelo(request):
    nasModelos = NasModelo.objects.all()
    context = {'nasModelos': nasModelos}

    return render(request, 'modelosNas/modNas_listar.html', context)

def agregarNasModelo(request):
    titulo = 'Agregar Modelo de NAS'

    if request.POST:
        forma = NasModeloForm(request.POST)
        if forma.is_valid():
            forma.save()
            return redirect('listar_modeloNas')
    else:
        forma = NasModeloForm()

    context = {'titulo': titulo, 'forma': forma}
    return render(request, 'modelosNas/modNas_form.html', context)

def actualizarNasModelo(request, id):
    titulo = 'Actualizar Modelo de NAS'
    nasmodelo = NasModelo.objects.get(id = id)

    if request.POST:
        forma = NasModeloForm(request.POST, instance=nasmodelo)
        if forma.is_valid():
            forma.save()
            return redirect('listar_modeloNas')
    else:
        forma = NasModeloForm(instance=nasmodelo)

    context = {'titulo': titulo, 'forma': forma}
    return render(request, 'modelosNas/modNas_form.html', context)


def eliminarNasModelo(request, id):
    nasmodelo = NasModelo.objects.get(id = id)
    nasmodelo.delete()
    return redirect('listar_modeloNas')


def listaDiscoModelo(request):
    discoModelos = DiscoModelo.objects.all()
    context = {'discoModelos': discoModelos}

    return render(request, 'modelosDiscos/modDiscos_listar.html', context)


def agregarDiscoModelo(request):
    titulo = 'Agregar Modelo de Disco'

    if request.POST:
        forma = DiscoModeloForm(request.POST)
        if forma.is_valid():
            forma.save()
            return redirect('listar_modeloDisco')
    else:
        forma = DiscoModeloForm()

    context = {'titulo': titulo, 'forma': forma}
    return render(request, 'modelosDiscos/modDiscos_form.html', context)


def actualizarDiscoModelo(request, id):
    titulo = 'Actualizar Modelo de Disco'
    discomodelo = get_object_or_404(DiscoModelo, id = id)

    if request.POST:
        forma = DiscoModeloForm(request.POST, instance=discomodelo)
        if forma.is_valid():
            forma.save()
            return redirect('listar_modeloDisco')
    else:
        forma = DiscoModeloForm(instance=discomodelo)

    context = {'titulo': titulo, 'forma': forma}
    return render(request, 'modelosDiscos/modDiscos_form.html', context)


def eliminarDiscoModelo(request, id):
    discomodelo = get_object_or_404(DiscoModelo, id = id)
    discomodelo.delete()
    return redirect('listar_modeloDisco')

