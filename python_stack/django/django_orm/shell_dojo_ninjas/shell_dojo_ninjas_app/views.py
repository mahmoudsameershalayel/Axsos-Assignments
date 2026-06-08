from django.shortcuts import render, redirect
from shell_dojo_ninjas_app.models import *

def index(request):
    dojos = Dojo.objects.prefetch_related('ninjas').all()
    return render(request, 'index.html', {'dojos': dojos})

def create_ninja(request):
    Ninja.objects.create(
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
        dojo_id=request.POST['dojo']
    )
    return redirect('/')

def create_dojo(request):
    Dojo.objects.create(
        name=request.POST['name'],
        city=request.POST['city'],
        state=request.POST['state']
    )
    return redirect('/')

def delete_dojo(request, dojo_id):
    Dojo.objects.get(id=dojo_id).delete()
    return redirect('/')