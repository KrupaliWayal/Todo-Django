from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from todo.models import TODOO
from django.contrib.auth.decorators import login_required


@login_required(login_url='/loginn')
def home(request):
    return render(request, 'signup.html')

def signup(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm', '').strip()
        emailid = request.POST.get('emailid', '').strip()
        pwd = request.POST.get('pwd', '')

        if not fnm or not emailid or not pwd:
            return render(request, 'signup.html', {'error': 'Please fill all fields.'})

        if User.objects.filter(username=fnm).exists():
            return render(request, 'signup.html', {'error': 'Username already taken.'})

        try:
            my_user = User.objects.create_user(username=fnm, email=emailid, password=pwd)
            my_user.save()
        except Exception as e:
            print('Error creating user:', e)
            return render(request, 'signup.html', {'error': 'Could not create user. Try again.'})

        return redirect('/loginn')

    return render(request, 'signup.html')


def loginn(request):
    if request.method == 'POST':
        fnm = request.POST.get('fnm')
        pwd = request.POST.get('pwd')

        userr = authenticate(request, username=fnm, password=pwd)
        if userr is not None:
            login(request, userr)
            return redirect('/todopage')
        else:
            return redirect('/loginn')

    return render(request, 'loginn.html')


@login_required(login_url='/loginn')
def todo(request):
    #Create
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        if title:
            TODOO.objects.create(title=title, user=request.user)

        return redirect('/todopage')  

    #Show
    res = TODOO.objects.filter(user=request.user).order_by('-date')
    return render(request, 'todo.html', {'res': res})


@login_required(login_url='/loginn')
def delete_todo(request, srno):
    obj = get_object_or_404(TODOO, srno=srno)
    obj.delete()
    return redirect('/todopage')


@login_required(login_url='/loginn')
def edit_todo(request, srno):
    obj = get_object_or_404(TODOO, srno=srno)

    #Update
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        if title:
            obj.title = title
            obj.save()
        return redirect('/todopage')

    #Show-Edit page
    res = TODOO.objects.filter(user=request.user).order_by('-date')
    return render(request, 'edit_todo.html', {'obj': obj, 'res': res})


def signout(request):
    logout(request)
    return redirect('/loginn')
