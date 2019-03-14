from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from .models import User, Address,Upper_category,Lower_category,Product_Info
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import bcrypt

# Create your views here.
def index(request):
    context={
            "upper_category":Upper_category.objects.all(),
            "product_info_pants":Product_Info.objects.filter(Upper_category=Upper_category.objects.filter(upper_name='PANTS'))[:4],
            "product_info_accessory":Product_Info.objects.filter(Upper_category=Upper_category.objects.filter(upper_name='ACCESSORY'))[:4],
            "product_info_outer":Product_Info.objects.filter(Upper_category=Upper_category.objects.filter(upper_name='OUTER'))[:3],
            "product_info_bag":Product_Info.objects.filter(Upper_category=Upper_category.objects.filter(upper_name='BAG'))[:4],
            "product_info_shoes":Product_Info.objects.filter(Upper_category=Upper_category.objects.filter(upper_name='SHOES'))[:5]
    }
    return render(request,"product_app/main.html",context)
#Go to register page
def go_register(request):
    return render(request,"product_app/register.html")

#get pants information
def get_pant_info(request,upper_cate_name):
    print(upper_cate_name)
    context={
            "upper_category":Upper_category.objects.all(),
            "product_info":Product_Info.objects.filter(Upper_category = Upper_category.objects.get(upper_name=upper_cate_name)),
    }
    return render(request,"product_app/all_product.html",context)

#Register user information
def register(request):
    if request.method =="POST":
        tFirst_name = request.POST["first_name"]
        tLast_name = request.POST["last_name"]
        tEmail= request.POST["email"]
        tPhone= request.POST["phone"]
        tPassword = bcrypt.hashpw(request.POST['password2'].encode(), bcrypt.gensalt())
        user=User.objects.create(first_name=tFirst_name,last_name=tLast_name,email=tEmail,phone_no=tPhone,password=tPassword)
        request.session['id']=user.id
        request.session['first_name']=tFirst_name
        return redirect("/")
def check_lower(request,upper_id):
    upper_category = Upper_category.objects.get(id=upper_id)
    context={
            "lower_category":Lower_category.objects.filter(Upper_category=upper_category),
            "upper_category":Upper_category.objects.all()
    }
    return render(request,"product_app/main.html",context)
#main page,product details function
def product_detail(request,product_id):
    context={
            "product_info":Product_Info.objects.get(id=product_id),
            "upper_category":Upper_category.objects.all(),
    }
    return render(request,"product_app/product_detail.html",context)

def get_upper_product(request,upper_id):
    context={
        "product_upper_info":Product_Info.objects.filter(Upper_category = Upper_category.objects.get(id=upper_id)),
        "upper_category":Upper_category.objects.all(),
    }
    return render(request,"product_app/all_product.html",context)

def go_cart(request,product_id):
    context={
        "product_info":Product_Info.objects.get(id=product_id),
    }
    return render(request,"product_app/cart_info.html",context)

def admin(request):
    return render(request,"admin_app/admin_login.html")