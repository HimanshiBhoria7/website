from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from app11.forms import Homeform,Studentform,Formstudent,Lip_Product



def index3(request):
    return HttpResponse("<h1> Hello get started with django </h1>")


def front(request):
    return render(request,'app11/front.html')

def front3(request):
    return HttpResponse("<h1> Nykaa broo </h1>")

def index(request):
    return render(request,'app11/index.html')


def home(request):
    forms = Homeform()
    return render(request,'app11/form.html',{'form':forms})

def student3(request):
    forms1 = Studentform()
    return render(request,'app11/form1.html',{'form1':forms1})

"""def student2(request):
    form3 = Formstudent()


    if request.method == 'POST':
        form = Formstudent(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return front(request)


        else:
            print('Error bro')

     return render(request,'app11/form.html',{'form':form})"""


def student(request):
    form = Formstudent()


    if request.method == 'POST':
        form = Formstudent(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return front(request)
        else:
            print("ERROR!")

    return render(request,'app11/user.html',{'form':form})

