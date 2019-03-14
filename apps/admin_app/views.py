from django.shortcuts import render,redirect
from apps.product_app.models import Upper_category,Lower_category,Product_Info,User
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Admin
from django.contrib import auth
from django.http import JsonResponse
from django.contrib import messages
import bcrypt

def index(request):
    product_info = Product_Info.objects.all()
    return render(request,"admin_app/admin_page.html",{'product_info':product_info})
    
#retrieve all product ,paging
#Author:Skyler 
#date:03/01/2019
def product_info(request):
    product_info = Product_Info.objects.all()
    paginator= Paginator(product_info,5)
    page = request.GET.get('page')
    try:
        product_info = paginator.page(page)
    except PageNotAnInteger:
        product_info = paginator.page(1)
    except EmptyPage:
        product_info = paginator.page(paginator.num_pages)
    context={
        'product_info':product_info,
        'upper_category':Upper_category.objects.all()
    }
    return render(request,"admin_app/admin_product_info.html",context)

#create new product 
def createNewProduct(request):
    errors = Product_Info.objects.product_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/product_info')
    else:
        tProduct_name = request.POST.get("product_name")
        tProduct_desc = request.POST.get("product_desc")
        tProduct_gender = request.POST.get("product_gender")
        tProduct_price = request.POST.get("product_price")
        tProduct_inventory = request.POST.get("product_inventory")
        tProduct_path = request.POST.get("product_path")
        tUpper_category_name = request.POST.get("upper_category")
        tLower_category_name= request.POST.get("lower_category")
        upper_category= Upper_category.objects.get(upper_name=tUpper_category_name)
        lower_category = Lower_category.objects.get(lower_name =tLower_category_name,Upper_category=upper_category)
        c=Lower_category.objects.get(id=4)
        Product_Info.objects.create(product_name=tProduct_name,product_desc=tProduct_desc,product_gender=tProduct_gender,product_price=tProduct_price,product_inventory=tProduct_inventory,product_path=tProduct_path,Upper_category=upper_category,Lower_category=lower_category)
    #return JsonResponse({'status': 2000, 'message': 'success insert data'})
        return redirect("/product_info")

#delete product
def delete_Product(request,product_id):
    context = {
        "register":Product_Info.objects.filter(id=f"{product_id}").delete()
    }
    return redirect("/product_info")

#update product ->show
#Author:Skyler 
#date:03/01/2019
def show_product(request,product_id):
    context = {
        "product_info":Product_Info.objects.get(id=f"{product_id}")
    }
    return render(request,"admin_app/admin_login.html",context)

#Create admin
def admin_register(request):
    tFirst_name = request.POST.get("first_name")
    tLast_name = request.POST.get("last_name")
    tEmail = request.POST.get("email")
    tPassword = bcrypt.hashpw(request.POST['password2'].encode(), bcrypt.gensalt())
    tAuthority = request.POST.get("authority")
    Admin.objects.create(admin_first_name=tFirst_name,admin_last_name=tLast_name,admin_email=tEmail,admin_password=tPassword,admin_authority=tAuthority)
    return redirect("/admin_register_page")

#Delete admin
def delete_admin(request,admin_id):
    Admin.objects.filter(id=f"{admin_id}").delete()
    return redirect("/admin_register_page")

#get lower category
def get_lower_category(request):
    upper_category_name = request.GET.get('upper_category') #upper name
    upper_category = Upper_category.objects.get(upper_name=upper_category_name)
    data = list(Lower_category.objects.filter(Upper_category =upper_category).values("lower_name"))
    return JsonResponse(data, safe=False)

#delte lower category
def delte_Category(request,category_id):
    Lower_category.objects.filter(id=f"{category_id}").delete()
    return redirect("/admin_category_management")

#create new category
def createNewLowerCategory(request):
    tUpper_category = request.POST.get("upper_category")
    upper_category = Upper_category.objects.get(upper_name=tUpper_category)
    Lower_category.objects.create(lower_name= request.POST.get("lower_category_name"),Upper_category=upper_category)
    return redirect("/admin_category_management")

#go to user mgmt page
def user_management(request):
    context={
        "user_info":User.objects.all()
    }
    return render(request,"admin_app/admin_user_manage.html",context)

#go to user register page
def user_register(request):
    errors = User.objects.user_login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/user_management')
    else:
        tFirst_name = request.POST.get("first_name")
        tLast_name = request.POST.get("last_name")
        tEmail = request.POST.get("email")
        tPhone = request.POST.get("phone")
        tPassword = bcrypt.hashpw(request.POST['password2'].encode(), bcrypt.gensalt())
        User.objects.create(first_name=tFirst_name,last_name=tLast_name,email=tEmail,phone_no=tPhone,password=tPassword)
        return redirect("/user_management")

#delete user
def delete_User(request,user_id):
    User.objects.filter(id=f"{user_id}").delete()
    return redirect("/user_management")

#Admin login page
def admin_login(request):
    if len(Admin.objects.filter(admin_email=request.POST['email']))>0:
        result = Admin.objects.filter(admin_email=request.POST['email'])
        if bcrypt.checkpw(request.POST['password'].encode(), result[0].admin_password.encode()):
            request.session['first_name']=result[0].admin_first_name
            request.session['authority'] = result[0].admin_authority
            request.session['id']=result[0].id
            return redirect('/admin_first_page')
        else:
            return render(request,"admin_app/admin_login.html")
    return render(request,"admin_app/admin_login.html")

#admin go to first page
def admin_first_page(request):
    context={
        "admin":Admin.objects.get(id=request.session['id'])
    }
    return render(request,"admin_app/admin_main.html",context)
def admin_register_page(request):
    context={
        "admin_info":Admin.objects.all()
    }
    return render(request,"admin_app/admin_register_page.html",context)
    
#admin go to category page
def admin_category_management(request):
    context={
        "upper_category":Upper_category.objects.all(),
        "lower_category":Lower_category.objects.all()
    }
    return render(request,"admin_app/admin_category.html",context)
def log_out(request):
    auth.logout(request)
    return render(request,"admin_app/admin_login.html")