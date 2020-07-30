from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import owners_temp,owners
from django.contrib import messages

# Create your views here.
def owner(request):
    if request.method=='POST':
        factory_name=request.POST['factory name']
        number1=request.POST['number1']
        number2=request.POST['number2']
        Distict=request.POST['Distict']
        Area=request.POST['Area']
        Address=request.POST['Address']
        description=request.POST['description']
        message=request.POST['message']
        amt_250=request.POST['message']
        print(amt_250,"************************")
        if amt_250=="no":
            amt_250=False
        else:
            amt_250=True
        amt_500=request.POST['message']
        print(amt_500,"************************")

        if amt_500=="no":
            amt_500=False
        else:
            amt_500=True
        amt_1000=request.POST['message']
        if amt_1000=="no":
            amt_1000=False
        else:
            amt_1000=True
        amt_can=request.POST['message']
        if amt_can=="no":
            amt_can=False
        else:
            amt_can=True
        des_can=request.POST['des_can']
        print(amt_250,amt_250)
        if owners_temp.objects.filter(contact_num1=number1).exists():
            messages.info(request,"contact 1 alreadty exists")
            return redirect('owner')
        elif owners_temp.objects.filter(contact_num2=number2).exists():
            messages.info(request,"contact 2 alreadty exists")
            return redirect('owner')
        else:
           obj=owners_temp(des_can=des_can,amt_500=amt_500,amt_can=amt_can,amt_1000=amt_1000,factory_name=factory_name,contact_num1=number1,contact_num2=number2,distict=Distict,area=Area,address=Address,desc=description,message=message,amt_250=amt_250)
           obj.save()
           messages.info(request,"SUCESSFULLY Register WE WILL CONTACT YOU SOON !")
           return redirect('owner')


    return render(request,'owner_reg.html')


def app(request):
    if request.method=='POST':
        inp=request.POST['submit']
        inp=inp.split('_')
        if inp[0]=="approve":
            addtemp=owners_temp.objects.get(contact_num1=inp[1])
            obj=owners(des_can=addtemp.des_can,amt_500=addtemp.amt_500,amt_can=addtemp.amt_can,amt_1000=addtemp.amt_1000,factory_name=addtemp.factory_name,contact_num1=addtemp.contact_num1,contact_num2=addtemp.contact_num2,distict=addtemp.distict,area=addtemp.area,address=addtemp.address,desc=addtemp.desc,message=addtemp.message,amt_250=addtemp.amt_250)
            obj.save()
            addtemp.delete()
            return redirect('app')
        else:
            addtemp=owners_temp.objects.get(contact_num1=inp[1])
            addtemp.delete()
            return redirect('app')


    else:
         own=owners_temp.objects.all()
         return render(request,'app.html',{'temps':own})
def watercos(request):
     own=owners.objects.all()

     return render(request,'watercos.html',{'own':own})
