from django.shortcuts import render, redirect
from . models import User
from . forms import UserForm
from django.contrib import messages

# Create your views here.

def users_list(request):
    
    users = User.objects.all().order_by('-date')
    return render(request, 'board/users.html',{'users':users})

def user_add(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_board')
    else:
        form = UserForm()
    return render(request,'board/add_user.html', {'form':form})

def user_view(request, name):
    user = User.objects.get(name = name)
    return render(request, 'board/view_user.html',{'user':user})

def user_edit(request, name):
    user = User.objects.get(name = name)
    if request.method == "POST":
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_board')
    else:
        form = UserForm(instance=user)
        return render(request,'board/edit_user.html',{'form':form, 'user':user})

def user_delete(request,name):
    user = User.objects.get(name=name)
    user.delete()
    #messages.success(request, f"User {name} has been deleted successfully.")
    return redirect('user_board')

