from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('id')
    return render(request,'main_index.html',{'title':'Главная страница','tasks':tasks})

def about(request):
    return render(request,'main_about.html')

def text_1(request):
    return HttpResponse("<h4>Prostoe zadanie"
                        "</h4>")

def info(request):
    return render(request,'main_info.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('')
        else:
            error = 'Форма была не верной'

    form = TaskForm()
    context = {
        'form':form,
        'error':error
    }
    return render(request,'main_create.html',context)



