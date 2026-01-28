from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegistroForm, PerfilForm, UserUpdateForm, ProfileUpdateForm, RegistroForm
from .models import Profile, Mensaje
from django.contrib.auth.models import User
from django.db.models import Q
# Vista de Registro
def signup(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Creamos el perfil automáticamente al registrarse
            Profile.objects.create(user=user)
            login(request, user)
            return redirect('home')
    else:
        form = RegistroForm()
    return render(request, 'accounts/signup.html', {'form': form})

# 1. Vista para VER el perfil
@login_required
def profile_view(request):
    # Aseguramos que el perfil exista
    Profile.objects.get_or_create(user=request.user)
    return render(request, 'accounts/profile.html')

# 2. Vista para EDITAR el perfil (el formulario)
@login_required
def profile_edit(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile') # Vuelve a la vista de perfil
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'accounts/profile_edit.html', {'u_form': u_form, 'p_form': p_form})

@login_required
def inbox(request):
    # Traemos mensajes donde yo sea el emisor O el receptor
    mensajes = Mensaje.objects.filter(
        Q(receptor=request.user) | Q(emisor=request.user)
    ).order_by('-fecha')
    return render(request, 'accounts/inbox.html', {'mensajes': mensajes})

@login_required
def enviar_mensaje(request, receptor_id=None): # Agregamos receptor_id opcional
    if request.method == 'POST':
        r_id = request.POST.get('receptor')
        contenido = request.POST.get('contenido')
        if r_id and contenido:
            receptor = User.objects.get(id=r_id)
            Mensaje.objects.create(emisor=request.user, receptor=receptor, contenido=contenido)
            return redirect('inbox')
    
    # Si venimos por el botón "Responder", ya sabemos quién es el receptor
    destinatario_fijo = None
    if receptor_id:
        destinatario_fijo = User.objects.get(id=receptor_id)

    usuarios = User.objects.exclude(id=request.user.id)
    return render(request, 'accounts/enviar_mensaje.html', {
        'usuarios': usuarios, 
        'destinatario_fijo': destinatario_fijo
    })

# EDITAR MENSAJE
@login_required
def editar_mensaje(request, pk):
    mensaje = get_object_or_404(Mensaje, pk=pk)
    
    # Seguridad: solo el que mandó el mensaje puede editarlo
    if mensaje.emisor != request.user:
        return redirect('inbox')

    if request.method == 'POST':
        contenido = request.POST.get('contenido')
        if contenido:
            mensaje.contenido = contenido
            mensaje.save()
            return redirect('inbox')
    
    return render(request, 'accounts/mensaje_edit.html', {'mensaje': mensaje})

# ELIMINAR MENSAJE
@login_required
def eliminar_mensaje(request, pk):
    mensaje = get_object_or_404(Mensaje, pk=pk)
    
    # Seguridad: solo el emisor puede borrar su rastro
    if mensaje.emisor == request.user:
        mensaje.delete()
        
    return redirect('inbox')