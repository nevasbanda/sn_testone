from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password == password1:
            if User.objects.filter(username=username).exist():
                print('Username exist try another one')
                return redirect(register)
            else:
                if User.objects.filter(email=email).exists():
                    print('Email exists try another one')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    user.save()
                    return redirect('login')
        else:
            print('Password did not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')
