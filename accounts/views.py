from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        # Passing the above data to the database
        if password1 == password2:
            # To check if the username is already taken
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('register')   # Return to the register after error occures
            elif User.objects.filter(email=email).exists(): # Checking if email is already taken
                messages.info(request, 'Email ID already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request,'Registered Successfully')
                # After registeration redirecting to the login page
                return redirect('login')
        else:
            messages.info(request,'Password not matching...')
            return redirect('register')
        return redirect('/')  # Redirecting back to the database
    else:
        return render(request,'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')



