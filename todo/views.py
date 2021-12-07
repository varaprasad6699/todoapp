from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import ToDoApp
from .form import AddForm
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.views.generic import ListView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def home(request):
    return render(request,'index.html')

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
               messages.info(request,"usere name is already taken")
               return redirect('/register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email is already  taken")
                return redirect('/register')
            else:
                user=User.objects.create_user(username=username,email=email,password=password1)
                user.save()
                return redirect('/login')
        else:
            messages.info(request,"passwords not maithing")
            return redirect('/register')
    return render(request,'register.html')

def loginPage(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user = auth.authenticate(username=username, password=password)
        print(user)
        if user is not None:
            print("inside")
            main_user=user
            auth.login(request, user)
            print("inside")
            return redirect('/')
            # A backend authenticated the credentials
        else:
            messages.info(request,"user credentials")
            return redirect('/login')
    return render(request,'loginpage.html')
def logout(request):
    auth.logout(request)
    return redirect("/")

@login_required(login_url='/login')
def addData(request):
    form=AddForm
    result={"form":form}
    if request.method=='POST':
        form=AddForm(request.POST)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author=request.user
            instance.save()
        return  HttpResponseRedirect('/todo/userdata/')
    return  render(request,'data/adddata.html',result)


class UpdateData(UpdateView):
    template_name='data/updatedata.html'
    model=ToDoApp
    fields=['desc']
    success_url='/todo/userdata/'

class DeleteData(DeleteView):
     template_name='data/todoapp_confirm_delete.html'
     model=ToDoApp
       
     success_url='/todo/userdata/'

@login_required(login_url='/login')
def userdata(request):    
    schedule_entries = ToDoApp.objects.filter(author=request.user)
    return render(request,'data/seedata.html',{"userdata":schedule_entries})