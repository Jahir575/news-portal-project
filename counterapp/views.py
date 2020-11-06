from django.shortcuts import render, get_object_or_404, redirect
from counterapp.models import Category, NewsData, Message, EmployeeModel
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

news_list = NewsData.objects.all().order_by('id').reverse()
newsslide = NewsData.objects.all().order_by('date')[:5]
latestnews = NewsData.objects.all().order_by('date')[:5]

nationaltop = NewsData.objects.filter(category=1)[:1]
national = NewsData.objects.filter(category=1)[1:]

International = NewsData.objects.filter(category=2)[1:]
Internationaltop = NewsData.objects.filter(category=2)[:1]

Games = NewsData.objects.filter(category=3)
Regional = NewsData.objects.filter(category=4)
LifeStyle = NewsData.objects.filter(category=5)

Technology = NewsData.objects.filter(category=6)[1:]
Technologytop = NewsData.objects.filter(category=6)[:1]

Business = NewsData.objects.filter(category=7)
Economics = NewsData.objects.filter(category=8)
Film = NewsData.objects.filter(category=9)
Music = NewsData.objects.filter(category=10)
Others = NewsData.objects.filter(category=11)


def home(request):

    context = {
        'news_list' : news_list,
        'newsslide' : newsslide,
        'latestnews' : latestnews,
        'national' : national,
        'nationaltop' : nationaltop,
        'Internationaltop' : Internationaltop,
        'International' : International,
        'Technologytop' : Technologytop,
        'Games' : Games,
        'Regional' : Regional,
        'LifeStyle' : LifeStyle,
        'Technology' : Technology,
        'Business' : Business,
        'Economics' : Economics,
        'Film' : Film,
        'Music' : Music,
        'Others' : Others,
        }
    return render(request,'pages/home.html', context)

def contact(request):
    context = {
        'news_list' : news_list,
        'newsslide' : newsslide,
    }
    return render(request,'pages/contact.html', context)

def details(request, news_pk):
    details = get_object_or_404(NewsData, pk = news_pk)
    related = NewsData.objects.filter(category=details.category).exclude( id=news_pk )[:3]
    context = {
        'details' : details,
        'related' : related,
        'newsslide' : newsslide,
    }
    return render(request,'pages/details.html', context)

def category(request, news_pk):
    
    all_category_news = NewsData.objects.filter(category=news_pk).order_by('id').reverse()

    context = {
        'all_category_news' : all_category_news,
        'news_pk' : news_pk,
    }
    return render(request,'pages/category.html', context)

def about(request):
    return render(request, 'pages/about.html' )

def message(request):
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    Message(name=name, email=email, message=message).save()
    return redirect(request.META['HTTP_REFERER'])

def adminlogin(request):
    return render(request, 'pages/adminlogin.html')

def adminauth(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(username=username, password=password)

    if user and username == 'jahir575':
        login(request, user)
        return redirect('adminloggedin')

    if user and username != 'jahir575':
        messages.add_message(request, messages.ERROR, "Your are not Authorised")
        return redirect(request.META['HTTP_REFERER'])

    if not user:
        messages.add_message(request, messages.ERROR, "Invalid Credentials")
        return redirect('adminlogin')

@login_required
def adminloggedin(request):
    context = {
        'news_list':news_list
    }
    return render(request, "pages/adminloggedin.html", context)

def adminlogout(request):
    logout(request)
    messages.add_message(request, messages.ERROR, "Logout Successful")
    return redirect('home')

def addemployee(request):
    if request.method == 'GET':
        return render(request, "pages/addemployee.html")
    else:
        try:
            user = User.objects.create_user(username=request.POST["employeename"], password=request.POST['password'])
            user.save()
            employeeid = 'EMPID'+str(20000+user.id)
            EmployeeModel(employee_id=employeeid, employee_name=request.POST["employeename"]).save()
            return redirect(request.META['HTTP_REFERER'])
        except IntegrityError:
            messages.add_message(request,messages.ERROR, "User Already Exist")
            return redirect(request.META['HTTP_REFERER'])
        
def employeelogin(request):
    return render(request, 'pages/employeelogin.html')


def employee_auth(request):
    employeename = request.POST['employeename']
    password = request.POST['password']

    user = authenticate(username=employeename, password=password)

    if user:
        login(request, user)
        return redirect('loggedin_employee')
    
    if not user:
        messages.add_message(request, messages.ERROE, "Wrong Credentials")
        return redirect(request.META['HTTP_REFERER'])
@login_required
def loggedin_employee(request):
    return render(request, 'pages/loggedin_employee.html')