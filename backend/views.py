from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Project, Profile, Phonathon_data
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth import login, authenticate
from rest_framework import viewsets
from rest_framework.parsers import JSONParser 
from backend.serializers import Phonathon_serializer
from backend.models import Phonathon_data
from rest_framework.decorators import api_view
import csv
# from rest_framework.decorators import api_view

# Create your views here.
def down(request):
    return HttpResponse("<h1>All the best for your exams!! We'll be back soon. :)</h1>")

def csv_profile(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['Email', 'Password', 'Full Name', 'Roll no', 'Department', 'Year of study', 'Mobile Number', 'Resume', 'Pref 1', 'Pref 2', 'Pref 3', 'Pref 4', 'Pref 5'])
    for profile in Profile.objects.all().values_list('email', 'password', 'fullname', 'rollno', 'department', 'yos', 'phoneno', 'resume', 'pref_1', 'pref_2', 'pref_3', 'pref_4', 'pref_5'):
        writer.writerow(profile)
    response['Content-Disposition'] = 'attachment; filename="profiles.csv"'
    return response

def csv_projects(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['id','title', 'details'])
    for profile in Project.objects.all().values_list('id','title', 'details'):
        writer.writerow(profile)
    response['Content-Disposition'] = 'attachment; filename="projects.csv"'
    return response

def home(request):
    return render(request, 'home.html')

def login1(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.filter(email=email).first()
        if user is None:
            context = {'message': 'User not found', 'class': 'danger'}
            return render(request, 'login.html', context)
        requested_profile = Profile.objects.filter(user=user).first()
        if password == requested_profile.password:
            if (requested_profile.submitted):
                context = {'message': 'Already submitted', 'class': 'danger'}
                return render(request, 'login.html', context)
            login(request, user)
            context = {'email': email}
            return redirect('projects')
        context = {'message': 'Incorrect Password', 'class': 'danger'}
        return render(request, 'login.html', context)
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        fullname = request.POST.get('fullname')
        rollno = request.POST.get('rollno')
        phoneno = request.POST.get('phoneno')
        password = request.POST.get('password')
        department = request.POST.get('dept')
        yos = request.POST.get('yos')
        resume = request.FILES['resume']
        # print(resume.name)
        # print(resume.size)
        check_user = User.objects.filter(email=email).first()
        if not email.split('@')[1]=='iitb.ac.in':
            context = {'message': 'Please login using your LDAP ID', 'class':'danger'}
            return render(request, 'register.html', context)
        if check_user:
            context = {'message': 'User already exists', 'class': 'danger'}
            return render(request, 'register.html', context)
        user = User(email=email, username=email)
        user.save()
        profile = Profile(user=user, password=password, fullname=fullname, rollno=rollno, phoneno=phoneno, department=department, yos=yos, email=email, resume=resume)
        profile.save()
        request.session['email'] = email
        request.session['fullname'] = fullname
        request.session['rollno'] = rollno
        request.session['phoneno'] = phoneno
        request.session['password'] = password
        return redirect('login1')
        
    return render(request, 'register.html')



def projects(request):
    context = {
        'projects': Project.objects.all()
    }
    return render(request, "projects.html", context)

def update(request):
    new = Project.objects.all()
    ids = new.values_list('pk', flat=True)
    profile = Profile.objects.get(user=request.user)
    error_msg = None
    c = 0
    for i in ids:
        preference = request.POST[str(i) + " preference"]
        if (preference != "0"):
            c = c+1
            for j in ids:
                if (j == i):
                    continue
                else:
                    pref_temp = request.POST[str(j) + " preference"]
                    if (pref_temp == preference):
                        error_msg = "Unique Preference required"
                    else:
                        continue

        else:
            continue
    if (c > 0):
        for i in ids:
            preference = request.POST[str(i) + " preference"]
            p = int(preference)
            if (p != 0):
                if p in range(1, c+1):
                    continue
                else:
                    error_msg = "Enter preference in order"
            else:
                continue
    else:
        error_msg = "Enter atleast one preference"

    if not error_msg:
        for i in ids:
            preference = request.POST[str(i) + " preference"]
            project = Project.objects.get(id=request.POST[str(i)])
            if (preference != "0"):
                if (preference == "1"):
                    profile.pref_1 = project.id
                elif (preference == "2"):
                    profile.pref_2 = project.id
                elif (preference == "3"):
                    profile.pref_3 = project.id
                elif (preference == "4"):
                    profile.pref_4 = project.id
                elif (preference == "5"):
                    profile.pref_5 = project.id
                profile.save()
            else:
                continue
        profile.submitted = True
        profile.save()
        return render(request, 'success.html')
    else:
        return render(request, 'projects.html', {'error': error_msg, 'projects': new})

@api_view(['POST'])
def Phonathon_save(request):
    if request.method=="POST":
        data = JSONParser().parse(request)
        serializer_data = Phonathon_serializer(data=data)
        if serializer_data.is_valid():
            serializer_data.save()
        # alum_id = request.POST.get("alum_id")
        # alum_name = request.POST.get("alum_name")
        # phone1 = request.POST.get("phone1")
        # phone2 = request.POST.get("phone2")
        # phone3 = request.POST.get("phone3")
        # duration = request.POST.get("duration")
        # stud_name = request.POST.get("stud_name")
        # data = Phonathon_data(alum_id=alum_id, alum_name=alum_name, phone1=phone1, phone2=phone2, phone3=phone3, duration=duration, stud_name=stud_name)
        # data.save()
        return HttpResponse("Posted Successfully")
    return HttpResponse("Thankyou")

class PhonathonViewSet(viewsets.ModelViewSet):
   queryset = Phonathon_data.objects.all()
   serializer_class = Phonathon_serializer
    
