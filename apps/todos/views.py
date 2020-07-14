from django.shortcuts import render, redirect
from django.http import HttpResponse
from todos.models import Todo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.http import require_http_methods
from .forms import NewTodoForm
from django.contrib import messages

# Create your views here.
@require_http_methods(["GET"])
def todos(request):
    todos_list = Todo.objects.all().order_by("-created_at")
    page_number = request.GET.get('page', 1)
    paginator = Paginator(todos_list, 2)

    try:
        todos = paginator.page(page_number)
    except PageNotAnInteger:
        todos = paginator.page(1)
    except EmptyPage:
        todos = paginator.page(paginator.num_pages)

    page_obj = paginator.get_page(page_number)
    
    return render(request=request,
                  template_name="main/todos.html",
                  context={"todos": todos})

@require_http_methods(["GET"])
def todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request=request,
                   template_name="main/todo.html",
                   context={"todo": todo})

@require_http_methods(["GET"])
def todo_update_form(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    form = NewTodoForm(instance=todo)
    return render(request=request,
                   template_name="main/todo-form.html",
                   context={"form": form, "todo":todo})

@require_http_methods(["POST"])
def todo_update_request(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    form = NewTodoForm(request.POST, instance=todo)
    if form.is_valid():
        form.save()
        title = form.cleaned_data["title"]
        messages.info(request, f"You updated todo with title {title}")
        return redirect("main:todos:todos")
