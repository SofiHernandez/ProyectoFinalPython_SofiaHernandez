from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    # --- Requisitos base ---
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='blogs/')

    # --- Información de la Actividad ---
    DIFICULTAD_CHOICES = [
        ('Baja', 'Baja'),
        ('Media', 'Media'),
        ('Alta', 'Alta'),
        ('N/A', 'No aplica'),
    ]
    dificultad = models.CharField(max_length=10, choices=DIFICULTAD_CHOICES, default='Baja')
    
    duracion = models.CharField(max_length=50, blank=True, help_text="Ej: 2 horas, Medio día")
    transporte = models.CharField(max_length=100, blank=True, help_text="Ej: Auto, Barco, 4x4")
    mejor_epoca = models.CharField(max_length=100, blank=True, help_text="Ej: Verano, Todo el año, Invierno") # <--- NUEVO
    requisitos = models.TextField(blank=True, help_text="Ej: Permiso de Parques, calzado técnico, entrada paga") # <--- NUEVO
    
    servicios = models.CharField(max_length=200, blank=True, help_text="Ej: Baños, WiFi, Parador")
    tips = models.TextField(blank=True, help_text="Consejos personales del autor")

    def __str__(self):
        return self.titulo
    
    # Esta función transforma el texto "Wifi, Baños, Guía" en una lista real
    def get_servicios_list(self):
        if self.servicios:
            return [s.strip() for s in self.servicios.split(',')]
        return []
    
class Mensaje(models.Model):
    emisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensajes_enviados")
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="mensajes_recibidos")
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"De {self.emisor.username} para {self.receptor.username}"