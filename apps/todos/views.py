from django.shortcuts import render
from django.http import HttpResponse
from todos.models import Todo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.http import require_http_methods
from .forms import NewTodoForm

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
def todo_form(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request=request,
                   template_name="main/todo.html",
                   context={"todo": todo})
