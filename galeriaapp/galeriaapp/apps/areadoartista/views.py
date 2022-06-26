from django.shortcuts import render, get_object_or_404, redirect
from .forms import AreadoartistaForm
from .models import Areadoartista
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/contas/login/')
def add_areadoartista(request):
    template_name = 'areadoartista/add_areadoartista.html'
    context = {}
    if request.method == 'POST':
        form = AreadoartistaForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('areadoartista:list_areadoartista')
    form = AreadoartistaForm()
    context['form'] = form
    return render(request, template_name, context)

def list_areadoartista(request):
    template_name = 'areadoartista/list_areadoartista.html'
    areadoartista = Areadoartista.objects.filter()
    context = {
        'areadoartista': areadoartista
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_areadoartista(request, id_areadoartista):
    template_name = 'areadoartista/add_areadoartista.html'
    context ={}
    areadoartista = get_object_or_404(Areadoartista, id=id_areadoartista)
    if request.method == 'POST':
        form = AreadoartistaForm(request.POST, instance=areadoartista)
        if form.is_valid():
            form.save()
            return redirect('areadoartista:list_areadoartista')
    form = AreadoartistaForm(instance=areadoartista)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_areadoartista(request, id_areadoartista):
    areadoartista = Areadoartista.objects.get(id=id_areadoartista)
    areadoartista.delete()
    return redirect('areadoartista:list_areadoartista')
