from django.db.models import Avg
from django.shortcuts import render,redirect
from .models import Doner,Ngo,Review
from django.contrib import messages
from .form import NgoregForm
def addngos(request):
    if request.method == "POST":
        form=NgoregForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            ngo=Ngo.objects.filter(status='Approved').all()
            return render(request,"index2.html",{"ngos":ngo})
        else:
            form=NgoregForm()
            return render(request,'addngos1.html',{'form':form})
    else:
        form=NgoregForm()
        return render(request,'addngos.html',{'form':form})
def home(request):
    ngo=Ngo.objects.filter(status="Approved").all()
    return render(request,"index.html",{"ngos":ngo})


def addngo(request):
    if request.method=='POST':
        n=Ngo()
        reg_no =request.POST['regno']
        n.reg_no =request.POST['regno']
        n.name =request.POST['name']
        n.specialization=request.POST['specialization']
        n.location=request.POST['location']
        n.ngo_logo=request.FILES['ngo_logo']
        n.address =request.POST['address']
        n.mobile =request.POST['mobile']
        n.description =request.POST['description']
        n.website=request.POST['website']
        n.state=request.POST['state']
        n.city=request.POST['city']
        n.status=False
        if Ngo.objects.filter(reg_no=reg_no).exists():
            messages.info(request,'already exist')
        else:
            n.save()
            ngo=Ngo.objects.filter(status="Approved").all()
            return render(request,"index2.html",{"ngos":ngo})
        
    else:
        return render(request,'addngo.html')
def search(request):
    specialization=request.POST['sp']
    ngo=Ngo.objects.filter(specialization=specialization).all()
    return render(request,"index1.html",{"ngos":ngo,'spcl':specialization})

def cityload(request):
    state=request.GET['name']
    cities = Ngo.objects.filter(state=state).values('city').distinct()
    return render(request, 'shows.html', {'cities': cities})

def finalshow(request):
    state=request.POST['state']
    city=request.POST['city']
    spcl=request.POST['spcl']
    print(state,city,spcl)
    ngo = Ngo.objects.filter(state=state,city=city,specialization=spcl).all()
    return render(request,"index.html",{"ngos":ngo})

def viewdetails(request):
    ng=request.GET['ngo']
    ngo=Ngo.objects.filter(reg_no=ng).get()
    id=ngo.id;
    re=Review.objects.filter(ngo_id=id).all().aggregate(Avg('rating'))
    comments=Review.objects.filter(ngo_id=id).all()
    return render(request,'viewngo.html',{'ngo':ngo,'rat':re,'comments':comments})
def reviews(request):
        n=Review()
        regno=request.POST['regno']
        ng=Ngo.objects.filter(reg_no=regno).get()
        n.ngo_id=ng.id
        n.name=request.POST['name']
        n.email=request.POST['email']
        n.rating=request.POST['stars']
        n.comment=request.POST['comment']
        n.save()
        return redirect('/')
def review(request):   
        ng=request.GET['regno']
        return render(request,'review.html',{'regno':ng})