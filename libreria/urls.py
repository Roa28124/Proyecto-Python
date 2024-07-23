from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('Marcas', views.Marcas, name='Marcas'),
    path('Marcas/crear', views.crear, name='crear'),
    path('Marcas/editar', views.editar, name='editar'),
    path('Marcas/eliminar/<int:id>', views.eliminar, name='eliminar'),
     path('Marcas/editar/<int:id>', views.editar, name='editar'),
 
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)