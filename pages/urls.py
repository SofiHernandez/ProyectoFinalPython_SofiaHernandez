from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('pages/', views.BlogListView.as_view(), name='pages'),
    path('pages/<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('about/', views.about, name='about'),
    path('pages/create/', views.BlogCreateView.as_view(), name='blog_create'),
    path('pages/<int:pk>/update/', views.BlogUpdateView.as_view(), name='blog_update'),
    path('pages/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='blog_delete'),
]