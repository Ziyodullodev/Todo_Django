from django.shortcuts import render, redirect
from .models import TodoModels
from django.http import HttpResponse
from .forms import TodoForms, UpdateTodo


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return HttpResponse(f"Sizning ip adresingiz: {ip}")


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