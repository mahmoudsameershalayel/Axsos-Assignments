from django.shortcuts import render, redirect
from semi_RESTFUL_TV_shows_app.models import Show
from django.contrib import messages

# Create your views here.
def router(request):
    return redirect('/shows/')
    
def index(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request, 'index.html', context)

def new_show(request):
    return render(request, 'new_show.html')

def create_show(request):
    if request.method != 'POST':
        return redirect('/shows/new/')

    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/shows/new/')
    else:
        Show.objects.create(
            title=request.POST['title'],
            network=request.POST['network'],
            release_date=request.POST['release_date'],
            description=request.POST.get('description', '')
        )
        return redirect('/shows/') 

def show_show(request, show_id):
    show = Show.objects.get(id=show_id)
    context = {
        'show': show
    }
    return render(request, 'show_show.html', context)

def edit_show(request, show_id):
    show = Show.objects.get(id=show_id)
    context = {
        'show': show
    }
    return render(request, 'edit_show.html', context)

def update_show(request, show_id):
    if request.method != 'POST':
        return redirect('/shows/new/')

    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{ show_id }/edit/')
    else:
        show = Show.objects.get(id=show_id)
        show.title = request.POST['title']
        show.network = request.POST['network']
        show.release_date = request.POST['release_date']
        show.description = request.POST['description']
        show.save()
        return redirect(f'/shows/{show_id}/')


def delete_show(request, show_id):
    show = Show.objects.get(id=show_id)
    show.delete()
    return redirect('/shows/')
