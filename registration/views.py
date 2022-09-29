from django.shortcuts import render, HttpResponseRedirect
from .forms import UserRagistrationForm, UserLoginForm, EditProfile
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import Group, User
# from django.contrib.auth.models import User
# log in 
def User_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
                form = UserLoginForm(request=request, data = request.POST)
                if form.is_valid():
                    uname = form.cleaned_data['username']
                    upass = form.cleaned_data['password']
                    user = authenticate(username = uname, password = upass)
                    if user is not None:
                        login(request, user)
                        messages.success(request, 'login successfully!!')
                        return HttpResponseRedirect('/dashboard/')          
        else:
            form = UserLoginForm()
        return render(request, 'login.html', {'fm':form})
    else:
        return HttpResponseRedirect('/dashboard/')

# registration  
def User_Regi(request):
    if request.method == 'POST':
        fm = UserRagistrationForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'acount created successfully!!')
            user = fm.save()
            group = Group.objects.get(name='user_group')
            user.groups.add(group)

    else:
        fm = UserRagistrationForm()
    return render(request, 'registration.html',{'fm':fm})



# logout 
def User_logout(request):
    logout(request)
    messages.success(request, 'logout successfully!!')
    return HttpResponseRedirect('/home/')


def user_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = EditProfile(request.POST, instance=request.user)
            if fm.is_valid():
                fm.save()
            messages.success(request, 'Profile Edit successfully!!')
            return HttpResponseRedirect('/dashboard/')
        else:
            fm = EditProfile(instance=request.user)

        return render(request, 'Edit_Profile.html', {'name':request.user,'fm':fm})
    else:
        return HttpResponseRedirect('/login/')