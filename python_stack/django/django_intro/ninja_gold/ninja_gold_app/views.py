import random
from datetime import datetime
from django.shortcuts import render, redirect


def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    context = {
        'gold': request.session['gold'],
        'activities': request.session['activities'],
    }
    return render(request, 'index.html', context)


def process_money(request):
    if request.method != 'POST':
        return redirect('index')

    location = request.POST['location']
    now = datetime.now()
    timestamp = now.strftime(f'%B {now.day} %Y {now.strftime("%I").lstrip("0") or "12"}:{now.strftime("%M")} {now.strftime("%p")}')

    if location == 'farm':
        amount = random.randint(10, 20)
        message = f'You entered a farm and earned {amount} gold. ({timestamp})'
        positive = True
    elif location == 'cave':
        amount = random.randint(10, 20)
        message = f'You entered a cave and earned {amount} gold. ({timestamp})'
        positive = True
    elif location == 'house':
        amount = random.randint(10, 20)
        message = f'You entered a house and earned {amount} gold. ({timestamp})'
        positive = True
    elif location == 'quest':
        amount = random.randint(-50, 50)
        if amount >= 0:
            message = f'You completed a quest and earned {amount} gold. ({timestamp})'
            positive = True
        else:
            message = f'You failed a quest and lost {abs(amount)} gold. Ouch. ({timestamp})'
            positive = False
    else:
        return redirect('index')

    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []

    request.session['gold'] += amount
    activities = request.session['activities']
    activities.insert(0, {'message': message, 'positive': positive})
    request.session['activities'] = activities
    request.session.modified = True

    return redirect('index')
