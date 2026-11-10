from django.shortcuts import render,redirect
from .models import*
# Create your views here.
def home(request):
    a=Available.objects.all()
    return render(request,'home.html',{'data':a})

def booking(request):
    user=request.user.username
    b=Booking.objects.filter(name=user)
    return render(request,'booking.html',{'data1':b})

def history(request):
    return render(request,'history.html')

def support(request):
    return render(request,'support.html')

def about(request):
    return render(request,'about.html')

def book(request,id):
    if request.method=='POST':
        if 'fcomp' in request.POST:
            a=request.POST["fcomp"]
            b=request.POST['fname']
            c=request.POST['fnum']
            d=request.POST['from']
            e=request.POST['to']
            f=request.POST['dtime']
            g=request.POST['fdate']
            h=request.POST['tprice']
            i=request.POST['yname']
            j=request.POST['email']
            k=request.POST['pnum']
            l=request.POST['aadhar']
            m=request.POST['age']
            n=request.POST['sclass']
            o=request.POST['snum']
            Booking.objects.create(
                comp=a,
                flightn=b,
                flightno=c,
                fromm=d,
                to=e,
                departure=f,
                date=g,
                price=h,
                name=i,
                email=j,
                age=m,
                seat=n,
                seatno=o,
                pnum=k,
                aadhar=l
            )
            return redirect('booking')
    a=Available.objects.get(id=id)
    return render(request,'book.html',{'i':a})

def update_(request,kd):
    if request.method=='POST':
        if 'yname' in request.POST:
            i=request.POST['yname']
            j=request.POST['email']
            k=request.POST['pnum']
            l=request.POST['aadhar']
            m=request.POST['age']
            n=request.POST['sclass']
            o=request.POST['snum'] 
            z=Booking.objects.get(id=kd)
            z.name=i
            z.email=j
            z.pnum=k
            z.aadhar=l
            z.age=m
            z.seat=n
            z.seatno=o
            z.save()
            return redirect('booking')
    a=Booking.objects.get(id=kd)
    return render(request,'update_.html',{'i':a})

def delete(request, pd):
    obj = Booking.objects.get(id=pd)
    obj.delete()
    return redirect('booking')