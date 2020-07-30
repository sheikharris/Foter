from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User ,auth
from django.contrib import messages
from .models import food,Popular_food
# Create your views here.
def index(request):
    return render(request,"index.html")

def About_Foter(request):
    return render(request,"About_Foter.html")

def Contact_us(request):
    return render(request,"Contact-us.html")

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['frist_name']
        last_name=request.POST['last_name']

        password1=request.POST['password1']
        email=request.POST['email']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username is already taken Dude,U are Late !")
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email id is already taken Dude,I think someone is using your Id! BE safe...")
                return redirect('signup')
            else:
                  user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                  user.save();
                  return redirect('login')
        else:
            messages.info(request,"password not maching Dude")
            return redirect('signup')


    else:
       return render(request,"SignUp.html")

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None :
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Username or Password is worng Dude! , try a bit you can remember!")
            return redirect("login")
    else:
        return render(request,'Login.html')

def logout(request):
    auth.logout(request)
    return redirect("/")

def rcfood(request):
    if request.method=='POST':
        op=request.POST['rb']
        foods=food.objects.all()
        l=len(foods)
        if l <=10:
           Popular_foods=foods.order_by('-rating')
        else :
           Popular_foods=foods.order_by('-rating')[:3]


        if op == 'cost':
           foods=foods.order_by('price')
        elif op == 'rating':
           foods=foods.order_by('-rating')
        elif op == 'time':
            foods=foods.order_by('location')
        elif op=='offer':
            pass




        return render(request,'recpage.html',{"Popular_foods":Popular_foods,"foods":foods})
    else :

        foods=food.objects.all()

        l=len(foods)
        if l <=10:
           Popular_foods=foods.order_by('-rating')
        else :
           Popular_foods=foods.order_by('-rating')[:3]

        foods=foods.reverse()
        return render(request,'recpage.html',{"Popular_foods":Popular_foods,"foods":foods})
