# core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Solicitud
from .forms import SolicitudForm

def home(request):
    """Página de inicio"""
    return render(request, 'core/home.html')

@login_required
def lista_solicitudes(request):
    """Lista las solicitudes del usuario logueado"""
    solicitudes = Solicitud.objects.filter(solicitante=request.user).order_by('-fecha_creacion')
    return render(request, 'core/lista_solicitudes.html', {'solicitudes': solicitudes})

@login_required
def crear_solicitud(request):
    """Crea una nueva solicitud"""
    if request.method == 'POST':
        form = SolicitudForm(request.POST)
        if form.is_valid():
            solicitud = form.save(commit=False)
            solicitud.solicitante = request.user
            solicitud.save()
            return redirect('lista_solicitudes')
    else:
        form = SolicitudForm()
    return render(request, 'core/crear_solicitud.html', {'form': form})

@login_required
def detalle_solicitud(request, id):
    """Muestra el detalle de una solicitud"""
    solicitud = get_object_or_404(Solicitud, id=id, solicitante=request.user)
    return render(request, 'core/detalle_solicitud.html', {'solicitud': solicitud})