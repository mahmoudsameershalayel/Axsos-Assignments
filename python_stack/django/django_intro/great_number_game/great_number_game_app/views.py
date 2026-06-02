import random
from django.shortcuts import render, redirect
from .models import Winner

def index(request):
    if 'secret_number' not in request.session:
        request.session['secret_number'] = random.randint(1, 100)
        request.session['attempts'] = 0
    return render(request, 'index.html')

def guess(request):
    secret = request.session.get('secret_number')
    request.session['attempts'] += 1
    attempts = request.session['attempts']
    user_guess = int(request.POST['guess'])
    if user_guess < secret:
        message = "Too low!"
    elif user_guess > secret:
        message = "Too high!"
    else:
        message = f"Correct! You guessed it in {attempts} attempt{'s' if attempts != 1 else ''}!"
        del request.session['secret_number']
        del request.session['attempts']
        return render(request, 'index.html', {'message': message, 'correct': True, 'attempts': attempts})

    if attempts >= 5:
        message = f"{secret} was the number!"
        del request.session['secret_number']
        del request.session['attempts']
        return render(request, 'index.html', {'message': message, 'lost': True})

    remaining = 5 - attempts
    return render(request, 'index.html', {'message': message, 'remaining': remaining})

def submit_winner(request):
    Winner.objects.create(name=request.POST['name'], attempts=int(request.POST['attempts']))
    return redirect('leaderboard')

def leaderboard(request):
    winners = Winner.objects.order_by('attempts', 'created_at')
    return render(request, 'leaderboard.html', {'winners': winners})
