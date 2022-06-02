from django.shortcuts import render, redirect
from .models import TodoModels
from django.http import HttpResponse
from .forms import TodoForms, UpdateTodo


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
    # form = UpdateTodo(instance=todo1)

    if request.method == "POST":
        post = request.POST.get('title')
        todo1.title = post
        todo1.save()
        # todo1 = TodoModels.objects.get(id=pk)
        print(post, pk)
        return redirect("/")

    context = {
        "tasks":todo,
        'edit':pk, 
        "form":todo1, 
        }
    print(pk)
    return render(request, "index.html", context)

def DeleteTodoView(request, pk):
    todo = TodoModels.objects.get(id=pk)
    todo.delete()
    return redirect("/")
    # context = {"form":todo}
    # return render(request, "delete-todo.html", context)


def Test(request):
    return HttpResponse("Salom bu test uchun edi")