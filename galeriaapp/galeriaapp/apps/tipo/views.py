from django.shortcuts import render, get_object_or_404, redirect
from .forms import TipoForm
from .models import Tipo
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/contas/login/')
def add_tipo(request):
    template_name = 'tipo/add_tipo.html'
    context = {}
    if request.method == 'POST':
        form = TipoForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('tipo:list_tipo')
    form = TipoForm()
    context['form'] = form
    return render(request, template_name, context)

def list_tipos(request):
    template_name = 'tipo/list_tipo.html'
    tipo = Tipo.objects.filter()
    context = {
        'tipo': tipo
    }
    return render(request, template_name, context)
@login_required(login_url='/contas/login/')
def edit_tipo(request, id_tipo):
    template_name = 'tipo/add_tipo.html'
    context ={}
    tipo = get_object_or_404(Tipo, id=id_tipo)
    if request.method == 'POST':
        form = TipoForm(request.POST, instance=tipo)
        if form.is_valid():
            form.save()
            return redirect('tipo:list_tipo')
    form = TipoForm(instance=tipo)
    context['form'] = form
    return render(request, template_name, context)
@login_required(login_url='/contas/login/')
def delete_tipo(request, id_tipo):
    tipo = Tipo.objects.get(id=id_tipo)
    tipo.delete()
    return redirect('tipo:list_tipo')
