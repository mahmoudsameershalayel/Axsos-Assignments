from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    request.session['visits'] = request.session.get('visits', 0) + 1
    if 'count' not in request.session:
        request.session['count'] = 0
    return render(request, 'index.html')

def increment_by_two(request):
    if 'count' in request.session:
        request.session['count'] += 2
    return redirect('/')

def increment_by_amount(request):
    amount = int(request.POST['amount'])
    if 'count' in request.session:
        request.session['count'] += amount
    return redirect('/')

def destroy_session(request):
    del request.session['count']
    del request.session['visits']
    return redirect('/')
