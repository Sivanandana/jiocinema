from django.shortcuts import render
from app.models import *
from django.http import HttpResponse,HttpResponseRedirect
from app.forms import *
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.



def registration(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'ufo':ufo,'pfo':pfo}
    if request.method=='POST':
        ufd=UserForm(request.POST)
        pfd=ProfileForm(request.POST)
        if ufd.is_valid() and pfd.is_valid():
            NSUO=ufd.save(commit=False)
            password=ufd.cleaned_data['password']
            NSUO.set_password(password)
            NSUO.save()
            NSPO=pfd.save(commit=False)
            NSPO.username=NSUO
            NSPO.save()
            send_mail('Registration',"Successfully Register in Jiocinema",'sivanandana2001@gmail.com',[NSUO.email],fail_silently=False)
            return HttpResponseRedirect(reverse('home'))
        else:
            return HttpResponse('Not valid')
    return render(request,'register_dummy1.html',d)

def home(request):
    return render(request,'home.html')

def login_form(request):
    if request.method=='POST':
        username=request.POST['un']
        password=request.POST['pw']

        AUO=authenticate(username=username,password=password)

        if AUO and AUO.is_active:
            login(request,AUO)
            request.session['username']=username
            return HttpResponseRedirect(reverse('home'))
        else:
            messages.success(request,'Invalid Username and Password')
            
    return render(request,'login_dummy1.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login_form'))


@login_required
def display_profile(request):
    username=request.session.get('username')
    US=User.objects.get(username=username)
    PO=Profile.objects.get(username=US)
    d={'US':US,'PO':PO}
    return render(request,'profile.html',d)

def free(request):
    return render(request,'free.html')

def news(request):
    return render(request,'news.html')

def sports(request):
    return render(request,'sports.html')
def subscribe(request):
    return render(request,'subscribe.html')
'''
@login_required
def change_password(request):
    if request.method=="POST":
        pw=request.POST['newPassword']
        username=request.session.get('username')
        UO=User.objects.get(username=username)
        UO.set_password(pw)
        UO.save()
        return HttpResponse('PASSWORD CHANGED SUCCESSFULLY')
    return render(request,'change_password.html')'''

def reset_password(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        LUO=User.objects.filter(username=username)
        if LUO:
            UO=LUO[0]
            UO.set_password(password)
            UO.save()
            return HttpResponseRedirect(reverse('log'))
        else:
            return HttpResponse ('INVALID CREDENTIALS')
    return render(request,'reset_password.html')



def log(request):
    return render(request,'login_dummy1.html')
def reg(request):
    return render(request,'register_dummy1.html')
def jiohome(request):
    return render(request,'jiocinemahome.html')