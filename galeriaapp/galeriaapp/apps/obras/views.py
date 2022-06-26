from django.shortcuts import render, get_object_or_404, redirect
from .forms import ObraForm
from .models import Obra
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/contas/login/')
def add_obra(request):
    template_name = 'obras/add_obras.html'
    context = {}
    if request.method == 'POST':
        form = ObraForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('obras:list_obras')
    form = ObraForm()
    context['form'] = form
    return render(request, template_name, context)


def list_obras(request):
    template_name = 'obras/list_obras.html'
    obras = Obra.objects.filter()
    context = {
        'obras': obras
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_obra(request, id_obra):
    template_name = 'obras/add_obras.html'
    context ={}
    obra = get_object_or_404(Obra, id=id_obra)
    if request.method == 'POST':
        form = ObraForm(request.POST, request.FILES,  instance=obra)
        if form.is_valid():
            form.save()
            return redirect('obras:list_obras')
    form = ObraForm(instance=obra)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_obra(request, id_obra):
    obra = Obra.objects.get(id=id_obra)
    obra.delete()
    return redirect('obras:list_obras')
