from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import Todo

# Create your views here.
def index(request):
    todo_items = Todo.objects.all().order_by("-added_date")
    return render(request, "main/index.html", {"todo_items": todo_items})


def add_todo(request):
    added_date = timezone.now()
    content = request.POST["content"]
    created_obj = Todo.objects.create(added_date=added_date, text=content)
    length_of_todos = Todo.objects.all().count()

    return HttpResponseRedirect(
        reverse(
            "main:index",
        )
    )


def delete_todo(request, todo_id):
    Todo.objects.get(id=todo_id).delete()

    return HttpResponseRedirect(
        reverse(
            "main:index",
        )
    )