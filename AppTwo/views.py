from django.shortcuts import render
from django.http import HttpResponse
from AppTwo.models import User
from AppTwo.forms import NewUserForm

def help(request):
    return render(request,'AppTwo/help.html')

def users(request):
    form = NewUserForm()
    if request.method == "POST":
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit = True)
            return help(request)
        else:
            print("Invalid Entry!!")

    return render(request,'AppTwo/users.html',{'form':form})
