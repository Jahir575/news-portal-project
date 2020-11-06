from django.shortcuts import render, get_object_or_404, redirect
from counterapp.models import Category, NewsData, Message
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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

    if not user and username != 'jahir575':
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
    employeename = request.POST['employeename']
    password = request.POST['password']

    user = User.objects.create_user(username=employeename, password=password)
    employeeid = 'EMPID'+str(200000+user.id)
    EmployeeModel(employee_id=employeeid, employee_name=employeename).save()
    return redirect(request.META['HTTP_REFERRER'])



