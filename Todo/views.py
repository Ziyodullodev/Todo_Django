from django.shortcuts import render, redirect
from .models import TodoModels

from .forms import TodoForms


def TodoView(request):

    todo = TodoModels.objects.all()
    form = TodoForms()

    if request.method == "POST":
        form = TodoForms(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/")
    list = {"list":todo, "form":form}
    return render(request, "home.html", list)


def UpdateTodoView(request, pk):
    todo = TodoModels.objects.get(id=pk)
    form = TodoForms(instance=todo)

    if request.method == "POST":
        form = TodoForms(request.POST, instance=todo)
        if form.is_valid():
            form.save()
        return redirect("/")

    context = {'form':form}
    return render(request, "update_todo.html", context)

def DeleteTodoView(request, pk):
    todo = TodoModels.objects.get(id=pk)
    if request.method == "POST":
        todo.delete()
        return redirect("/")
    context = {"form":todo}
    return render(request, "delete-todo.html", context)