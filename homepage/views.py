from django.shortcuts import render
from homepage.models import Course , Mentor
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.


def index(request):
    return render(request,"index.html")


def course(request):
    if request.method == 'POST':
        c_code = request.POST['code'] 
        c_desc = request.POST['desc']
        data = Course(code=c_code, description=c_desc) 
        data.save()
        mycourse = Course.objects.all().values()
        message = 'Data Saved Successfully'
        dict = {
            'message': message,
            'mycourse': mycourse,
        }
    else:
        dict = {
            'message': ''
        }
    
    return render(request, "course.html", dict)

def mentor(request):
    if request.method == 'POST':
        m_id = request.POST.get('id')
        m_name = request.POST.get('name')
        m_roomno = request.POST.get('roomno')
        data= Mentor(menid=m_id, menname=m_name, menroomno=m_roomno)
        data.save()
        mymentor = Mentor.objects.all().values()
        message = 'Data Saved'
        dict = {
              'message' : message,
              'mymentor': mymentor,
         }
    else:
         dict = {
              'message' : ''
         }
    return render (request,"mentor.html", dict)

def update_course(request,code):
    data=Course.objects.get(code=code)
    dict = {
        'data':data,
    }
    return render (request, "update_course.html", dict)

def save_update_course(request,code):
    c_desc= request.POST['desc']
    data=Course.objects.get(code=code)
    data.description = c_desc
    data.save()
    return HttpResponseRedirect(reverse("course"))

def update_mentor(request,menid):
    data=Mentor.objects.get(menid=menid)
    dict = {
        'data':data,
    }
    return render (request, "update_mentor.html", dict)

def save_update_mentor(request,menid):
    m_name = request.POST['name']
    m_roomno = request.POST['roomno']
    data=Mentor.objects.get(menid=menid)
    data.menname = m_name
    data.menroomno = m_roomno
    data.save()
    return HttpResponseRedirect(reverse("mentor"))

def delete_course(request,code):
    data = Course.objects.get(code=code)
    data.delete()
    return HttpResponseRedirect(reverse('course'))

def delete_mentor(request,menid):
    data = Mentor.objects.get(menid=menid)
    data.delete()
    return HttpResponseRedirect(reverse('mentor'))

def search_course(request):
    if request.method == 'GET':
        c_code = request.GET.get ('c_code')

        if c_code:
            data = Course.objects.filter(code=c_code.upper())
        else:
            data = None

        context = {
            'data' : data
        }

        return render (request, "search_course.html", context)
    
    return render(request, "search_course.html")