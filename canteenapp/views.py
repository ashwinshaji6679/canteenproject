from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.core import serializers
from django.conf import settings
from django.core.mail import send_mail,EmailMessage
import os


from .models import *
# Create your views here.
def logout(request):
    return render(request, "login.html", {})
def forgot(request):
    return render(request, "forgot.html", {})
def show_order_admin(request):
    return render(request,"order_view.html", {})
def Bill_view(request):
    return render(request,"bill_view.html", {})
def Cart(request):
    return render(request,"cart.html", {})
def food_view_user(request):
    return render(request,"menu.html", {})
def Food_view_user(request):
    return render(request,"Food_view_user.html", {})
def View_daily_item_page(request):
    return render(request,"day_food.html", {})
def food_item(request):
    return render(request,"add_food_item.html", {})
def add_food_item(request):
    return render(request, "view_food.html", {})
def display_login(request):
    return render(request, "login.html", {})
def Display_login(request):
    return render(request, "login.html", {})
def reg(request):
    return render(request, "register.html", {})
def home_user(request):
    return render(request, "user1.html", {})
def admin_home(request):
    return render(request, "admin.html", {})
def Show_user(request):
    return render(request, "showuser.html", {})
def stats_view(request):
    return render(request, "stats.html", {})
def forgot_password(request):
    return render(request, "forgot_password.html", {})
def send_password(request):
     email = request.GET.get("email")
     print(email)
     if ulogin1.objects.filter(email=email).exists():
        i=ulogin1.objects.get(email=email)
        password=str(i.password)
        username=str(i.username)
        subject='Forgot Password Request'
        content='Greetings from FoodKart-ACMS MITS ✌\n\nIn response to your request,furnishing your Account Credentials below:\n\nUsername --> '+username+'\nPassword --> '+password+'\n\n😋 Keep Fooding!\n\n\nFor any queries contact:\n\n\tfoodkart.acms.mits@gmail.com\n\n 🛑 NB: Please keep this mail strictly confidential 🛑'
        send_mail(subject, content, settings.EMAIL_HOST_USER, [email], auth_user=settings.EMAIL_HOST_USER, auth_password=settings.EMAIL_HOST_PASSWORD)
        return HttpResponse("Success")
     else:
         return HttpResponse("Email is not registered with us")
def user_reg(request):
    name=request.GET.get("name")
    email=request.GET.get("email")
    password=request.GET.get("password")
    college_id=request.GET.get("college_id")
    username=request.GET.get("username")
    c=ulogin1.objects.filter(college_id=college_id,password=password)
    if c:
        return HttpResponse("Already Registered")
    elif name=="" or password=="" or username=="" or email=='' or college_id=='':
        return HttpResponse("Please fill out all the fields") 
    else:
        v=ulogin1(name=name,password=password,username=username,email=email,college_id=college_id)
        v.save()
        return HttpResponse("Registration Successfull !!")
   
def check_login(request):
    username = request.GET.get("uname")
    password= request.GET.get("password")
    print(username)
    i=ulogin1.objects.filter(username=username,password=password)
    print(i)
    request.session['id']=password
    c=i.count()
    print(c)
    if c==1:          
        return HttpResponse("user login")
    elif username=='ADMIN' and password=='ADMIN':
        return HttpResponse("admin login")
    else:
        return HttpResponse("Invalid")
def showuser(request):
    try:
         v1=ulogin1.objects.all()
         print(v1,"d")
         data={}
   
         if v1:
          valu=serializers.serialize("json",v1)
          data['d1']=json.loads(valu)
          return JsonResponse(data,safe=False)
         else:
           return HttpResponse("no data")
    except Exception as e:
        print(e)
        return HttpResponse("error") 
def store_food_item(request):
    name = request.GET.get("name")
    price = request.GET.get("price")
   
    i=food.objects.filter(name=name.title())
    #request.session['username']=var1
    c=i.count()
    #print(c)
    if name=="" or price=="":
        return HttpResponse("Please Fill Out All Fields")
    elif c==1:          
        return HttpResponse("Item Already Added")
    else:
        v=food(name=name.title(),price=price)
        v.save()
        return HttpResponse("Item Successfully Added")
def view_food(request):
    try:
         v1=food.objects.all()
         print(v1,"d")
         data={}
   
         if v1:
          valu=serializers.serialize("json",v1)
          data['d1']=json.loads(valu)
          return JsonResponse(data,safe=False)
         else:
           return HttpResponse("no data")
    except Exception as e:
        print(e)
        return HttpResponse("error") 
        
def day_food(request):
    name = request.GET.get("name")
    price = request.GET.get("price")
    plate = request.GET.get("plate")
    time = request.GET.get("time")
    from datetime import datetime
    now=datetime.now()
  
    o=now.strftime("%m/%d/%Y") 
    i=dayfood1.objects.filter(name=name,date=o)
    #request.session['username']=var1
    c=i.count()
    #print(c)
    if c==1:          
        return HttpResponse("Already added to Today's Menu")
    else:
        v=dayfood1(name=name,date=o,price=price,plate=plate)
        v.save()
        return HttpResponse("Successfully Added to Today's Menu")

def edit_food(request):
    name = request.GET.get("name")
    price = request.GET.get("price")
    id2 = request.GET.get("id2")

    obj=food.objects.get(key=id2)
    obj.name=name
    obj.price=price

    obj.save()
    return HttpResponse("Item Edited Successfully")

def deleteevent(request):
    try:
        ci=request.GET.get("id2")
        print(ci)
        t=food.objects.get(key=ci)
        t.delete()
        return HttpResponse("Successfully deleted food items")
    except Exception as e:
        print(e)
        return HttpResponse("error")
def Day_food_view(request):
    from datetime import datetime
    now=datetime.now() 
    o=now.strftime("%m/%d/%Y") 
    x= now.strftime("%H:%M:%S")
    day=now.strftime("%a")

    print(now.strftime("%H:%M:%S"))
    x = datetime.strptime(x,"%H:%M:%S")
    y = datetime.strptime('00:10:00',"%H:%M:%S")
    y1= datetime.strptime('23:30:00',"%H:%M:%S")
    
    if day=='Sun':
        return HttpResponse("holiday")
    if x>y and x<y1:
         v1=dayfood1.objects.filter(date=o)
         print(v1,"d")
         data={}
         if v1:
          valu=serializers.serialize("json",v1)
          data['d1']=json.loads(valu)
          return JsonResponse(data,safe=False)
         else:
          return HttpResponse("no data")
    elif x<y:
          return HttpResponse("not started")
    else:
          return HttpResponse("ended")
def Aday_food_view(request):
         from datetime import datetime
         now = datetime.now()
         o=now.strftime("%m/%d/%Y") 

         v1=dayfood1.objects.filter(date=o)
         print(v1,"d")
         data={}
         if v1:
          valu=serializers.serialize("json",v1)
          data['d1']=json.loads(valu)
          return JsonResponse(data,safe=False)
         else:
          return HttpResponse("no data")
from datetime import datetime 
def order_food(request):
    from datetime import datetime
    user=request.session['id']
    user_name=ulogin1.objects.get(college_id=user)
    user_name1=user_name.name
    now = datetime.now()
    current_time = now.strftime("%I:%M")
    o=now.strftime("%m/%d/%Y") 
    name = request.GET.get("name")
    price = request.GET.get("price")
    id2 = request.GET.get("id2")
    quantity = request.GET.get("quantity")
    v=dayfood1.objects.get(key=id2)
    v1=v.plate
    v2=v.time
    v4=int(v1)-int(quantity)
    
    if v4>=0:
        if cart.objects.filter(item=name,date=o).exists():
            return HttpResponse("Food item already ordered today. Cannot order today")

        v.plate=str(v4)
        v.save()
        v1=cart(name=user_name1,item=name,price=price,quantity=quantity,date=o,time=current_time,expire='')
        v1.save()
        if v4==0:
            dayfood1.objects.get(key=id2).delete()

        return HttpResponse("Item Added to Cart")
    else:
         return HttpResponse("Not Enough Plates Remaining") 
def cart_view(request):
    now = datetime.now()
    current_time = now.strftime("%I:%M")
    o=now.strftime("%m/%d/%Y") 
    user=request.session['id']
    user_name=ulogin1.objects.get(college_id=user)
    user_name1=user_name.name
    try:
         v1=cart.objects.filter(name=user_name1,date=o)
         print(v1,"d")
         data={}
   
         if v1:
          valu=serializers.serialize("json",v1)
          data['d1']=json.loads(valu)
          return JsonResponse(data,safe=False)
         else:
           return HttpResponse("no data")
    except Exception as e:
        print(e)
        return HttpResponse("error") 
def bill(request):
    import string
    import random
    global stat_price
    now = datetime.now()
    o=now.strftime("%m/%d/%Y") 
    current_time = now.strftime("%I:%M")
    user=request.session['id']
    user_name=ulogin1.objects.get(college_id=user)
    user=user_name.name
    res = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k = 6))
   
    k=cart.objects.filter(name=user,date=o)
    k1=k.count()
    m=[]
    c=[]
    p=[]
    l=[]
    pr=0
    for i in range(0,k1):
       k2=k[i].item
       k3=k[i].quantity
       k4=k[i].price      
       price=int(k3)*int(k4)   
       pr=pr+price
       t=[k2,k3,k4,price,pr,res]
       p.append(k2)
       c.append(t)
       m.append(k3)
       l.append(k4)
    # s=bill2.objects.filter(name=user,time=current_time,date=o)
    # if s:
    # else:
    l1=bill5(name=user,item=p,quan=m,qprice=l,price=pr,ids=str(res),time=current_time,date=o,status='not paid',use='not used')
    l1.save()
    stat_price=price
   
    return JsonResponse(c,safe=False)
def delete(request):
   ci=request.GET.get("id2")
   v=cart.objects.get(key=ci)
   item=v.item
   qnt=v.quantity
   now = datetime.now()
   o=now.strftime("%m/%d/%Y")
   
   if dayfood1.objects.filter(name=item,date=o).exists():
    obj2=dayfood1.objects.get(name=item,date=o)
    print(obj2.plate)
    obj2.plate=str(int(obj2.plate)+int(qnt))
    obj2.save()
   else:
    k=food.objects.get(name=item)
    price=k.price
    z1=dayfood1(name=item,date=o,price=price,plate=str(qnt))
    z1.save()

   v.delete()
  
  
   return HttpResponse("deleted") 
def cancel(request):
   ci=request.GET.get("number")
   v=bill5.objects.get(ids=ci)
   v.delete()
   # v1=bill3.objects.get(ids=ci)
   # v1.delete()
   return HttpResponse("cancelled") 
def pay(request):
   ci=request.GET.get("number")
   am=request.GET.get("amount")
  
   f=bill5.objects.get(ids=ci)
   f.status='paid'
   f.save()
   v=bill5.objects.get(ids=ci)
   v2=v.date
   # v.delete()
   user=request.session['id']
   user_name=ulogin1.objects.get(college_id=user)
   user=user_name.name
   cart.objects.filter(name=user,date=v2).delete()
   update_stats()
   return HttpResponse("removed") 

def update_stats():
    now = datetime.now()
    o=now.strftime("%d/%m/%Y") 
    if stats1.objects.filter(date=o).exists():
     q1=stats1.objects.get(date=o)
     t=q1.amount
     val=int(t)+stat_price
     q1.amount=str(val)
     q1.save()
    else:
     q2=stats1(date=o,amount=stat_price)
     q2.save()

def Order_admin_view(request):
         from datetime import datetime
         now = datetime.now()
         o=now.strftime("%m/%d/%Y") 
         v1=bill5.objects.filter(date=o,status='paid').order_by('time')
         print(v1,"d")
         data={}
         if v1:
          valu=serializers.serialize("json",v1)
          data['d1']=json.loads(valu)
          return JsonResponse(data,safe=False)
         else:
          return HttpResponse("no data")   
def User_bill(request):
         from datetime import datetime
         now = datetime.now()
         o=now.strftime("%m/%d/%Y") 
         user=request.session['id']
         user_name=ulogin1.objects.get(college_id=user)
         user=user_name.name
         v1=bill5.objects.filter(name=user,status='paid').order_by('-key')
         print(v1,"d")
         data={}
         if v1:
          valu=serializers.serialize("json",v1)
          data['d1']=json.loads(valu)
          return JsonResponse(data,safe=False)
         else:
          return HttpResponse("no data")   
def View_bill(request):
   ci=request.GET.get("number")
   v=bill5.objects.filter(ids=ci)
   data={}
   if v:
          valu=serializers.serialize("json",v)
          data['d1']=json.loads(valu)
          return JsonResponse(data,safe=False)
   else:
          return HttpResponse("no data")   
def Delete_bill(request):
   ci=request.GET.get("number")
   v=bill5.objects.get(ids=ci)
   v.use='used'
   v.save()
  
   return HttpResponse("food collected")   
def Remove_bill(request):
   ci=request.GET.get("number")
   v=bill5.objects.get(ids=ci)
   k=v.use
   if k=='used':
     v.use='deleted'
     v.delete()
  
     return HttpResponse("Bill deleted Successfully")   
   else:
     return HttpResponse("food is not collected yet")   
def statistics(request):
         v1=stats1.objects.all().order_by('-date')
         print(v1,"d")
         data={}
         if v1:
          valu=serializers.serialize("json",v1)
          data['d1']=json.loads(valu)
          return JsonResponse(data,safe=False)
         else:
          return HttpResponse("no data")
def search_date(request):
    o=request.GET.get("date")
    try:
         v1=stats1.objects.filter(date=o)
         print(v1,"d")
         data={}
   
         if v1:
          valu=serializers.serialize("json",v1)
          data['d1']=json.loads(valu)
          return JsonResponse(data,safe=False)
         else:
           return HttpResponse("no data")
    except Exception as e:
        print(e)
        return HttpResponse("error") 

def decrement(request):
        ci=request.GET.get("id2")
        v=cart.objects.get(key=ci)
        item=v.item
        qnt=v.quantity
        now = datetime.now()
        o=now.strftime("%m/%d/%Y")
        
        if dayfood1.objects.filter(name=item,date=o).exists():
            obj2=dayfood1.objects.get(name=item,date=o)
            print(obj2.plate)
            obj2.plate=str(int(obj2.plate)+1)
            obj2.save()
            obj3=cart.objects.get(key=ci)
            v4=int(obj3.quantity)-1
            obj3.quantity=str(int(obj3.quantity)-1)
            print(obj3.quantity)
            obj3.save()
            if v4==0:
                cart.objects.get(key=ci).delete()
            return HttpResponse("Decremented")
        else:
            k=food.objects.get(name=item)
            price=k.price
            z1=dayfood1(name=item,date=o,price=price,plate=1)
            z1.save()
            obj3=cart.objects.get(key=ci)
            v4=int(obj3.quantity)-1
            obj3.quantity=str(int(obj3.quantity)-1)
            print(obj3.quantity)
            obj3.save()
            if v4==0:
                cart.objects.get(key=ci).delete()
            return HttpResponse("Decremented")

def increment(request):
            ci=request.GET.get("id2")
            v=cart.objects.get(key=ci)
            item=v.item
            qnt=v.quantity
            now = datetime.now()
            o=now.strftime("%m/%d/%Y")
            
            if dayfood1.objects.filter(name=item,date=o).exists():
                obj2=dayfood1.objects.get(name=item,date=o)
                print(obj2.plate)
                v4=int(obj2.plate)-1
                obj2.plate=str(int(obj2.plate)-1)
                obj2.save()
                obj3=cart.objects.get(key=ci)
                obj3.quantity=str(int(obj3.quantity)+1)
                print(obj3.quantity)
                obj3.save()
                if v4==0:
                   dayfood1.objects.get(name=item,date=o).delete()
                return HttpResponse("Incremented")
            else:
                return HttpResponse("Out of Stock") 

def Increment_menu(request):
    ci=request.GET.get("id2")
    now=datetime.now()
    o=now.strftime("%m/%d/%Y") 
    obj3=dayfood1.objects.get(key=ci,date=o)
    obj3.plate=str(int(obj3.plate)+1)
    print(obj3.plate)
    obj3.save()
    return HttpResponse("Incremented")

def Decrement_menu(request):
    ci=request.GET.get("id2")
    now=datetime.now()
    o=now.strftime("%m/%d/%Y") 
    obj3=dayfood1.objects.get(key=ci,date=o)
    obj3.plate=str(int(obj3.plate)-1)
    print(obj3.plate)
    obj3.save()
    if obj3.plate==0:
        dayfood1.objects.get(key=id2).delete()
    return HttpResponse("Incremented")

def Delete_menu(request): 
    ci=request.GET.get("id2")
    now=datetime.now()
    o=now.strftime("%m/%d/%Y") 
    dayfood1.objects.get(key=ci,date=o).delete()
    return HttpResponse("Deleted from Menu")
    
