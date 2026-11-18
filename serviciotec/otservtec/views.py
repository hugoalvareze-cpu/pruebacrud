from django.shortcuts import render, get_object_or_404, redirect, redirect
from .models import OrdenTrabajo, Equipo, Zona, Tecnico, Cliente, Bateria, Cliente, Equipo, Zona
from .forms import OrdenTrabajoForm, ClienteForm, EquipoForm, ZonaForm, BateriaForm
from django.contrib.auth.decorators import login_required

#base
def base(request):
    return render(request, 'base.html')

def inicio(request):
    return render(request, 'inicio.html')

#lista ot

def ot_total(request):
    # Obtiene todas las órdenes de trabajo registradas
    ordentrabajo = OrdenTrabajo.objects.filter(id_estado__estado__iexact='ok').order_by('-fecha_ingreso')
    return render(request, 'ot_total.html', {'ordentrabajo': ordentrabajo})

def ot_list(request):
    ordentrabajo = OrdenTrabajo.objects.exclude(id_estado__estado__iexact='ok').order_by('-fecha_ingreso')
    return render(request, 'ot_list.html', {'ordentrabajo': ordentrabajo})

def lista_retiro_ot(request):
    # Obtiene solo las órdenes de trabajo cuyo estado sea 'ok' (o 'OK')
    ordentrabajo = OrdenTrabajo.objects.filter(id_estado__estado__iexact='ok', fecha_retiro__isnull=True).order_by('-fecha_ingreso')
    
    return render(request, 'lista_retiro_ot.html', {'ordentrabajo': ordentrabajo})

def lista_cliente(request):
    clientes = Cliente.objects.all()
    return render(request, 'lista_cliente.html', {'clientes': clientes})

def lista_zona(request):
    zonas = Zona.objects.all()
    return render(request, 'lista_zona.html', {'zonas': zonas})

def lista_equipo(request):
    equipos = Equipo.objects.all()   
    return render(request, 'lista_equipo.html', {'equipos': equipos})

def lista_bateria(request):
    baterias = Bateria.objects.all()
    return render(request, 'lista_bateria.html', {'baterias': baterias})
  
def lista_tecnicos(request):
    tecnicos = Tecnico.objects.all()
    return render(request, 'lista_tecnicos.html', {'tecnicos': tecnicos})


#agregar ot

@login_required
def form_agregar_ot(request):
    if request.method == 'POST':
        form = OrdenTrabajoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ot_list')
    else:
        form = OrdenTrabajoForm()
    return render(request, 'form_agregar_ot.html', {'form': form})

@login_required
def form_agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_cliente')
    else:
        form = ClienteForm()
    return render(request, 'form_agregar_cliente.html', {'form': form})

@login_required
def form_agregar_zona(request):
    if request.method == 'POST':
        form = ZonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_zona')
    else:
        form = ZonaForm()
    return render(request, 'form_agregar_zona.html', {'form': form})

@login_required
def form_agregar_equipo(request):
    if request.method == 'POST':
        form = EquipoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_equipo')
    else:
        form = EquipoForm()
    return render(request, 'form_agregar_equipo.html', {'form': form})

@login_required
def form_agregar_bateria(request):
    if request.method == 'POST':
        form = BateriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_bateria')
    else:
        form = BateriaForm()
    return render(request, 'form_agregar_bateria.html', {'form': form})


#modificar ot
@login_required
def form_modificar_ot(request, pk):   
    ot = get_object_or_404(OrdenTrabajo, pk=pk)    
    if request.method == 'POST':        
        form = OrdenTrabajoForm(request.POST, instance=ot)
        if form.is_valid():
            form.save()
            return redirect('ot_list') # O a la vista que prefieras
    else:
        form = OrdenTrabajoForm(instance=ot)   
    context = {'form': form, 'ot': ot}
    return render(request, 'form_modificar_ot.html', context)


@login_required
def form_modificar_retiro(request, pk):  # <-- Agrega 'pk' como argumento
    ot = get_object_or_404(OrdenTrabajo, pk=pk)
    
    if request.method == 'POST':
        form = OrdenTrabajoForm(request.POST, instance=ot)
        if form.is_valid():
            form.save()
            return redirect('lista_retiro_ot')
    else:
        form = OrdenTrabajoForm(instance=ot)
    
    context = {
        'form': form,
        'ot': ot
    }
    return render(request, 'form_modificar_retiro.html', context)


@login_required
def form_modificar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_cliente')
    else:
        form = ClienteForm(instance=cliente)
    
    return render(request, 'form_modificar_cliente.html', {'form': form, 'cliente': cliente})

@login_required
def form_modificar_zona(request, pk):
    zona_obj = get_object_or_404(Zona, pk=pk)
    if request.method == 'POST':
        form = ZonaForm(request.POST, instance=zona_obj)
        if form.is_valid():
            form.save()
            return redirect('lista_zona')
    else:
        form = ZonaForm(instance=zona_obj)
    
    return render(request, 'form_modificar_zona.html', {'form': form, 'zona': zona_obj})

@login_required
def form_modificar_equipo(request, pk):
    equipo = get_object_or_404(Equipo, pk=pk)
    if request.method == 'POST':
        form = EquipoForm(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
            return redirect('lista_equipo')
    else:
        form = EquipoForm(instance=equipo)
    
    return render(request, 'form_modificar_equipo.html', {'form': form, 'equipo': equipo})

@login_required
def form_modificar_bateria(request, pk):
    bateria = get_object_or_404(Bateria, pk=pk)
    if request.method == 'POST':
        form = BateriaForm(request.POST, instance=bateria)
        if form.is_valid():
            form.save()
            return redirect('lista_bateria')
    else:
        form = BateriaForm(instance=bateria)
    
    return render(request, 'form_modificar_bateria.html', {'form': form, 'bateria': bateria})




def vista_form_ot(request, pk):
    ot = get_object_or_404(OrdenTrabajo, pk=pk)
    return render(request, 'vista_form_ot.html', {'ot': ot})