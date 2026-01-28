from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares/', null=True, blank=True)
    descripcion = models.TextField(blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"

class Mensaje(models.Model):
    emisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="enviados")
    receptor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recibidos")
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensaje de {self.emisor.username} para {self.receptor.username}"
