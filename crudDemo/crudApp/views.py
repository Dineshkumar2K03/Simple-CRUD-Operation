from django.shortcuts import render,redirect
from crudApp.models import student
from crudApp.forms import studentForm
# Create your views here.

def retrieve_view(request):
    Student = student.objects.all()
    return render(request,'crudApp/index.html',{'student':Student})

def create_view(request):
    form = studentForm()
    if request.method =='POST':
        form = studentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/check')
    
    return render(request,'crudApp/create.html',{'form':form})

def delete_view(request,id):
    Student = student.objects.get(id=id)
    Student.delete()
    return redirect('/check')


    