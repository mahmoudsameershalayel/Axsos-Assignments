from django.shortcuts import render, redirect
from login_and_registration_app.models import User
from django.contrib import messages
import bcrypt

# Create your views here.
def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method != 'POST':
        return redirect('/')

    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        password = request.POST['password']
        hashed_pass =  bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            birth_date=request.POST['birth_date'],
            email=request.POST['email'],
            password=hashed_pass,
        )
        request.session['userid'] = user.id
        return redirect('/success')

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.filter(email = email)
    if user:
        logged_user = user[0]
        result = bcrypt.checkpw(password.encode(), logged_user.password.encode())
        if result:
            request.session['userid'] = logged_user.id
            return redirect('/success')
    return redirect('/')

def success(request):
    user_id = request.session.get('userid')

    if not user_id:
        return redirect('/')

    user = User.objects.get(id=user_id)

    return render(request, 'success.html', {'name': user.first_name})