from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Por ahora dejamos las de login/logout configuradas con las de Django
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('messages/', views.inbox, name='inbox'),
    path('messages/enviar/', views.enviar_mensaje, name='enviar_mensaje'),
    path('messages/enviar/<int:receptor_id>/', views.enviar_mensaje, name='enviar_mensaje_a'),
    path('messages/edit/<int:pk>/', views.editar_mensaje, name='editar_mensaje'),
    path('messages/delete/<int:pk>/', views.eliminar_mensaje, name='eliminar_mensaje'),
]
