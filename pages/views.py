from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView, UpdateView, DeleteView
from .models import Blog
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy


# Para el inicio (El Hero gigante del Lago Lácar)
class HomeView(ListView):
    model = Blog  # <--- ESTO ES LO QUE DICE QUE FALTA
    template_name = 'pages/home.html'
    context_object_name = 'blogs'
    
    def get_queryset(self):
        return Blog.objects.all().order_by('-fecha')[:4]

# Para la lista de viajes (Las tarjetas estilo Voyage)
class BlogListView(ListView):
    model = Blog
    template_name = 'pages/blog_list.html'
    context_object_name = 'blogs'

# Para el detalle inmersivo (Línea de tiempo e iconos)
class BlogDetailView(DetailView):
    model = Blog
    template_name = 'pages/blog_detail.html'

# Para el "Acerca de mí"
def about(request):
    return render(request, 'pages/about.html')


class BlogCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Blog
    template_name = 'pages/blog_form.html'
    # Incluimos todos los campos que mencionaste
    fields = [
    'titulo', 'subtitulo', 'cuerpo', 'imagen', 
    'dificultad', 'duracion', 'transporte', 
    'mejor_epoca', 'requisitos', 'servicios', 'tips']
    success_url = '/pages/'

    def test_func(self):
        return self.request.user.is_superuser

    # ESTO ES LO QUE FALTA:
    def form_valid(self, form):
        form.instance.autor = self.request.user # Asigna automáticamente al usuario logueado
        return super().form_valid(form)

# Vista para EDITAR un destino (Solo para el Admin)
class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    template_name = 'pages/blog_form.html' # Reutilizamos el diseño de crear
    fields = ['titulo', 'subtitulo', 'cuerpo', 'imagen', 'dificultad', 'duracion', 'transporte', 'mejor_epoca', 'requisitos', 'servicios', 'tips']
    success_url = reverse_lazy('pages') # Al terminar, vuelve al listado

    def test_func(self):
        return self.request.user.is_superuser
    
class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    template_name = 'pages/blog_confirm_delete.html' # El cartel de "¿Estás seguro?"
    success_url = reverse_lazy('pages') # Si borra, lo manda a la lista principal

    def test_func(self):
        return self.request.user.is_superuser
    