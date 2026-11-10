from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def login_(request):
    if request.method == 'POST':
        username = request.POST['uname']
        password = request.POST['pasw']
        u = authenticate(username = username,password=password)#return me object
        if u:
            login(request,u)#login fun is used to create session storage
            return redirect('home')
        else:
            return render(request,'login_.html',{'error':'username or password is wrong..!'})
    return render(request,'login_.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        username = request.POST['uname']
        password = request.POST['pasw']
        try:
            u = User.objects.get(username = username)
            return render(request,'register.html',{'error':'username is already taken'})
        except:
            User.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                email = email,
                username = username,
                password = password
            )
            return redirect('login_')
    return render(request,'register.html')

# Create your views here.
def profile(request):
    return render(request,'profile.html')

def logout_(request):
    logout(request)
    return redirect('login_')

def update(request):
    print(request.user)
    user = User.objects.get(username = request.user)
    print(user.email)
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        username = request.POST['uname']
        user.first_name = first_name
        user.last_name  = last_name
        user.email = email
        user.username = username
        user.save()
        return redirect('profile')
    return render(request,'update.html',{'data':user})

def fpasw(request):
    if request.method == 'POST':
        if 'uname' in request.POST:
            username = request.POST['uname']
            try:
                user = User.objects.get(username = username)
                request.session['fpuser'] = user.username
                return render(request,'fpasw.html',{'new':True})
            except:
                return render(request,'fpasw.html',{'error':True})
        
        if 'pasw' in request.POST:
            username = request.session.get('fpuser')
            user = User.objects.get(username = username)
            new_pasw  = request.POST['pasw']
            user.set_password(new_pasw)
            user.save()
        
    return render(request,'fpasw.html')