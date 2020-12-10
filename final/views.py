from django.contrib.auth import logout, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Forum
from .forms import Former
# Create your views here.


def final(request):
    return render(request, 'index.html')


def index(request):
    question = Forum.objects.all()
    context = {'question': question}
    return render(request, 'index.html', context)


def createt(request):
       form = Former(request.POST or None)
       if form.is_valid():
        form.save()
        return redirect('index')
       else:
        return render(request,'create_ques.html',{'form':form})

def editt(request,id):
    question = Forum.objects.get(id=id)
    form = Former(request.POST or None, instance=question)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request,'edit_form.html',{'form':form, 'question':question})

def loginuser(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            redirect('index')
    else:
        form = AuthenticationForm()

    return render(request,'login.html', {'form':form})


def logoutuser(request):
    logout(request)
    return redirect('index')


def account(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request,'account.html',{'form':form})

def resource(request):
    return render(request, 'resource.html')

def deletet(request,id):
    question = Forum.objects.get(id=id)
    if request.method == 'POST':
        question.delete()
        return redirect('index')
    return render(request, 'deletet.html', {'question': question})