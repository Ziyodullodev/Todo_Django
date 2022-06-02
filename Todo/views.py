from django.shortcuts import render, redirect
from .models import TodoModels
from django.http import HttpResponse
from .forms import TodoForms, UpdateTodo
# from django.contrib.gis.geoip2 import GeoIP2

def get_client_ip(request):
    user = request.user.id
    resp = HttpResponse(f"Sizning ip adresingiz: {user}")
    resp.set_cookie(key='user', value=user, httponly=True)
    return resp


def TodoView(request):
    todo = TodoModels.objects.all()
    # form = TodoForms()
    if request.method == "POST":
        form = TodoForms(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    list = {
        "tasks":todo,
         }
    return render(request, "index.html", list)


def UpdateTodoView(request, pk):
    todo = TodoModels.objects.all()
    todo1 = TodoModels.objects.get(id=pk)

    if request.method == "POST":
        post = request.POST.get('title')
        todo1.title = post
        todo1.save()
        return redirect("/")

    context = {
        "tasks":todo,
        'edit':todo1.title, 
        }
    return render(request, "index.html", context)

def DeleteTodoView(request, pk):
    todo = TodoModels.objects.get(id=pk)
    todo.delete()
    return redirect("/")

def ComplatedTask(request, pk):
    todo = TodoModels.objects.get(id=pk)
    todo.complate = False
    todo.save()
    print("end", todo.complate)
    return redirect("/")

def StartTask(request, pk):
    todo = TodoModels.objects.get(id=pk)
    todo.complate = True
    todo.save()
    print("start", todo.complate)
    return redirect("/")