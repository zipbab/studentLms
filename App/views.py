from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from App.models import Student
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.core.paginator import Paginator

# ================Fontend Section====================
# function to render the home page
def frontend(request):
    return render(request, "frontend.html")

# ================Backend Section=====================
# function to render the backend page
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def backend(request):
    if 'q' in request.GET:
        q = request.GET['q']
        all_student_list = Student.objects.filter(
            Q(name=q) | Q(phone=q) | Q(email=q) | Q(dateofbirth=q) | Q(gender=q) | Q(grade=q) | Q(note=q) 
        ).order_by('-grade')
    else : 
        all_student_list = Student.objects.all().order_by('-grade')

    paginator = Paginator(all_student_list, 10)
    page = request.GET.get('page')
    all_student = paginator.get_page(page)

    return render(request, 'backend.html', {"students" : all_student})     

# Function to Add student
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def add_student(request):
    if request.method == "POST":
        if request.POST.get('name') \
            and request.POST.get('phone') \
            and request.POST.get('email') \
            and request.POST.get('dateofbirth') \
            and request.POST.get('gender') \
            and request.POST.get('grade') \
            or request.POST.get('note'):
            student = Student()
            student.name = request.POST.get('name')
            student.phone = request.POST.get('phone')
            student.email = request.POST.get('email')
            student.dateofbirth = request.POST.get('dateofbirth')
            student.gender = request.POST.get('gender')
            student.grade = request.POST.get('grade')
            student.save()
            messages.success(request, "Student added successfully !!!")
            return HttpResponseRedirect('/backend')
    else:
            return render(request, "add.html")

# function to delete sutdent
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def delete_student(request, student_id):
    student = Student.objects.get(id = student_id)
    student.delete()
    messages.success(request, "Student removed Successfully !")
    return HttpResponseRedirect('/backend')

# function to access to student individually
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def student(request, student_id):
    student = Student.objects.get(id = student_id)
    if student != None:
        return render(request, "edit.html", {'student' : student})


# function to edit the student
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url="login")
def edit_student(request):
    if request.method == "POST":
        student = Student.objects.get(id = request.POST.get('id'))
        if student != None:

            student.name = request.POST.get('name')
            student.phone = request.POST.get('phone')
            student.email = request.POST.get('email')
            student.dateofbirth = request.POST.get('dateofbirth')
            student.gender = request.POST.get('gender')
            student.grade = request.POST.get('grade')
            student.note = request.POST.get('note')
            student.save()

            messages.success(request, "Student updated Successfully !")
            return HttpResponseRedirect('/backend')


