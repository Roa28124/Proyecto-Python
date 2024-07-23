from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import marca
from .forms import MarcaForm
def inicio(request):
     return render(request, 'paginas/inicio.html')
def nosotros(request):
    return render(request, 'paginas/nosotros.html')
def Marcas(request):
    Marcas=marca.objects.all()
    print(Marcas)
    return render(request, 'Marcas/index.html', {'Marcas':Marcas})
def crear(request):
    formulario=MarcaForm(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('Marcas')
    return render(request, 'Marcas/crear.html', {'formulario':formulario})
def editar(request,id):
    Marca=marca.objects.get(id=id)
    formulario=MarcaForm(request.POST or None, request.FILES or None, instance=Marca)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('Marcas')
    return render(request, 'Marcas/editar.html', {'formulario': formulario})




def eliminar(request,id):
    Marca=marca.objects.get(id=id)
    Marca.delete()
    return redirect('Marcas')
