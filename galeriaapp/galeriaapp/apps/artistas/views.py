from django.shortcuts import render, get_object_or_404, redirect
from .forms import ArtistaForm
from .models import Artista, Areadoartista, ArtistaAreadoartista
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/contas/login/')
def add_artista(request):
    template_name = 'artistas/add_artista.html'
    context = {}
    if request.method == 'POST':
        form = ArtistaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('artistas:list_artistas')
    form = ArtistaForm()
    context['form'] = form
    return render(request, template_name, context)


def list_artistas(request):
    template_name = 'artistas/list_artistas.html'
    artista_areadoartista = ArtistaAreadoartista.objects.filter()
    areadoartista = Areadoartista.objects.filter()
    artistas = Artista.objects.filter()
    context = {
        'artistas': artistas,
        'areadoartista': areadoartista,
        'artista_areadoartista': artista_areadoartista
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_artista(request, id_artista):
    template_name = 'artistas/add_artista.html'
    context ={}
    artista = get_object_or_404(Artista, id=id_artista)
    if request.method == 'POST':
        form = ArtistaForm(request.POST, instance=artista)
        if form.is_valid():
            form.save()
            return redirect('artistas:list_artistas')
    form = ArtistaForm(instance=artista)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_artista(request, id_artista):
    artista = Artista.objects.get(id=id_artista)
    artista.delete()
    return redirect('artistas:list_artistas')
