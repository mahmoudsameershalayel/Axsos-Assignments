from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def submit_survey(request):
    context = {
        'name': request.POST['user_name'],
        'dojo_location': request.POST['location'],
        'favorite_language': request.POST['language'],
        'experience': request.POST.get('experience', 'Not selected'),
        'interests': request.POST.getlist('interests'),
        'comment': request.POST['comment'],
    }
    return render(request, 'result.html', context)
