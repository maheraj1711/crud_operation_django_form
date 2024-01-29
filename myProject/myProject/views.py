from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from myApp.models import *
from myProject.forms import *
# Create your views here.
def myDashboard(request):

    
    return render(request,'dashboard.html')

def signupPage(request):
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("singinPage")
    else:
        
        form=CustomUserCreationForm()

    return render(request,'signup.html',{'form':form})


def signinPage(request):
    if request.method=='POST':
        form=CustomAuthenticationForm(request,data=request.POST)

        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('myDashboard')
    else:
        form=CustomAuthenticationForm()
    return render(request,'signin.html',{'form':form})

def logoutpage(request):

    return redirect('signinPage')


def teacherHome(request):
    teacher=teacherModel.objects.all()
    form=teacherForm

    context={
        'teacher':teacher,
        'form':form,
    }


    return render(request,'teacherHome.html',context)

def teacherAdd(request):
    if request.method=='POST':
        form=teacherForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("teacherHome")

def teacherDelete(request,myid):
    teacher=teacherModel.objects.get(id=myid).delete()
    # teacher.delete()
    return redirect("teacherHome")

def teacherEdit(request,myid):
    teacher=teacherModel.objects.get(id=myid)
    form=teacherForm(instance=teacher)

    if request.method=='POST':
        form=teacherForm(request.POST,instance=teacher)
        form.save()
        return redirect("teacherHome")

    return render(request,'teacherEdit.html',{'form':form})


def studentHome(request):

    student=studentModel.objects.all()
    form=studentForm

    context={
        'student':student,
        'form':form,
    }


    return render(request,'studentHome.html',context)


def studentAdd(request):
    if request.method=='POST':
        form=studentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("studentHome")
        
def studentDelete(request,myid):
    student=studentModel.objects.get(id=myid).delete()
    # student.delete()
    return redirect("studentHome")

def studentEdit(request,myid):
    student=studentModel.objects.get(id=myid)
    form=studentForm(instance=student)

    if request.method=='POST':
        form=studentForm(request.POST,instance=student)
        form.save()
        return redirect("studentHome")

    return render(request,'studentEdit.html',{'form':form})




def staffHome(request):

    staff=staffModel.objects.all()
    form=staffForm

    context={
        'staff':staff,
        'form':form,
    }


    return render(request,'staffHome.html',context)


def staffAdd(request):
    if request.method=='POST':
        form=staffForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("staffHome")
        
def staffDelete(request,myid):
    staff=staffModel.objects.get(id=myid).delete()
    # staff.delete()
    return redirect("staffHome")

def staffEdit(request,myid):
    staff=staffModel.objects.get(id=myid)
    form=staffForm(instance=staff)

    if request.method=='POST':
        form=staffForm(request.POST,instance=staff)
        form.save()
        return redirect("staffHome")

    return render(request,'staffEdit.html',{'form':form})


def doctorHome(request):

    doctor=doctorModel.objects.all()
    form=doctorForm

    context={
        'doctor':doctor,
        'form':form,
    }


    return render(request,'doctorHome.html',context)


def doctorAdd(request):
    if request.method=='POST':
        form=doctorForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("doctorHome")
        
def doctorDelete(request,myid):
    doctor=doctorModel.objects.get(id=myid).delete()
    # doctor.delete()
    return redirect("doctorHome")

def doctorEdit(request,myid):
    doctor=doctorModel.objects.get(id=myid)
    form=doctorForm(instance=doctor)

    if request.method=='POST':
        form=doctorForm(request.POST,instance=doctor)
        form.save()
        return redirect("doctorHome")

    return render(request,'doctorEdit.html',{'form':form})


def nurseHome(request):


    return render(request,'nurseHome.html')

def nurseHome(request):

    nurse=nurseModel.objects.all()
    form=nurseForm

    context={
        'nurse':nurse,
        'form':form,
    }


    return render(request,'nurseHome.html',context)


def nurseAdd(request):
    if request.method=='POST':
        form=nurseForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("nurseHome")
        
def nurseDelete(request,myid):
    nurse=nurseModel.objects.get(id=myid).delete()
    # nurse.delete()
    return redirect("nurseHome")

def nurseEdit(request,myid):
    nurse=nurseModel.objects.get(id=myid)
    form=nurseForm(instance=nurse)

    if request.method=='POST':
        form=nurseForm(request.POST,instance=nurse)
        form.save()
        return redirect("nurseHome")

    return render(request,'nurseEdit.html',{'form':form})


def employeeHome(request):

    employee=employeeModel.objects.all()
    form=employeeForm

    context={
        'employee':employee,
        'form':form,
    }


    return render(request,'employeeHome.html',context)


def employeeAdd(request):
    if request.method=='POST':
        form=employeeForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("employeeHome")
        
def employeeDelete(request,myid):
    employee=employeeModel.objects.get(id=myid).delete()
    # employee.delete()
    return redirect("employeeHome")

def employeeEdit(request,myid):
    employee=employeeModel.objects.get(id=myid)
    form=employeeForm(instance=employee)

    if request.method=='POST':
        form=employeeForm(request.POST,instance=employee)
        form.save()
        return redirect("employeeHome")

    return render(request,'employeeEdit.html',{'form':form})