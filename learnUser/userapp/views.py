from django.shortcuts import render
from userapp.forms import UserForm,UserProfileInfoForm
from django.contrib.auth import authenticate,logout,login
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from userapp.models import UserProfileInfo
# Create your views here.
def index(req):
    return render(req,'userapp/index3.html')

@login_required
def user_logout(req):
    logout(req)
    return render(req,'userapp/check.html')

def register(req):

    registered=False

    if req.method=="POST":
        user_form=UserForm(data=req.POST)
        profile_form=UserProfileInfoForm(data=req.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.set_password(user.password) #method for hash
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user

            if 'profile_pic' in req.FILES:     #files get pic pdfs
                profile.profile_pic=req.FILES['profile_pic']
            profile.save()

            registered=True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form=UserForm()
        profile_form=UserProfileInfoForm()

    return render(req,'userapp/registration3.html',{'user_form':user_form,
                                                    'profile_form':profile_form,
                                                    'registered':registered})


def user_login(req):
    if req.method=='POST':
        username=req.POST.get('username')
        password=req.POST.get('password')
        user=authenticate(username=username,password=password)
        req.session['username'] = username
        if user:
            if user.is_active:
                username = req.session['username']
                login(req,user)
                return render(req,'userapp/check.html',{'username':username})
            else:
                return HttpResponse("not active")
        else:
            print("someone tried to login and faild")
            print("username:{} and password{}".format(username,password))
            return HttpResponse("invalid login detail")
    else:
        return render(req,'userapp/login3.html',{})

def gallery(req):
    if req.method == 'GET':
    #profile_form = UserProfileInfoForm(data=req.POST)
        img = UserProfileInfo.objects.all()
        return render(req,'userapp/gallery.html',{'img':img})
    