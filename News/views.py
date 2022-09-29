from django.shortcuts import render, HttpResponseRedirect
from .forms import NewsForm
from .models import News
from django.contrib import messages

# Home Page
def HomeCall(request):
    newss = News.objects.all()
    return render(request, 'home.html', {'fm':newss})
 
# about Page
def AboutCall(request):
    user = request.user
    full_name = user.get_full_name()
    return render(request, 'about.html' ,{'fn':full_name})
 
# contact Page
def ContactCall(request):
    return render(request, 'contact.html')
 
# dashboard Page
def DashboardCall(request):
    if request.user.is_authenticated:
        newss = News.objects.all()

        user = request.user
        return render(request, 'dashboard.html', {'fm':newss, 'user':user})
    else:
        return HttpResponseRedirect('/home/')


def AddNews(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            fm = NewsForm(request.POST)
            if fm.is_valid():
                messages.success(request, 'News Added successfully!!')
                fm.save()
                return HttpResponseRedirect('/dashboard/')
        else:
            fm = NewsForm()
        return render(request, 'AddNews.html', {'fm':fm})
    else:
        return HttpResponseRedirect('/home/')

def DeleteNews(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            member = News.objects.get(pk=id)
            member.delete()
            messages.success(request, 'News deleted successfully!!')
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/home/')


def EditNews(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = News.objects.get(pk=id)
            fm = NewsForm(request.POST, instance=pi)
            if fm.is_valid():
                fm.save()
                messages.success(request, 'Update News successfully!!')
                return HttpResponseRedirect('/dashboard/')
        else:
            pi = News.objects.get(pk=id)
            fm = NewsForm(instance=pi)
        return render(request, 'editnews.html', {'fm':fm})
    else:
        return HttpResponseRedirect('/home/')


