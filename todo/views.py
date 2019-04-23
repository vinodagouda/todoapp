from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ToDoCreateForm
from todo.models import ToDoDetails
from django.http import HttpResponseRedirect
from django.urls import reverse

@login_required(login_url="")
def login_success(request):
    data = {}
    data['user'] = request.user
    data['todos'] = []
    to_dos = ToDoDetails.objects.filter(user=request.user)
    
    for to_do in to_dos:
        todo_data = {}
        todo_data['id'] = to_do.id
        todo_data['title'] = to_do.title
        todo_data['description'] = to_do.description
        data['todos'].append(todo_data)
    
    return render(request, "todo-home.html", data)

@login_required(login_url="")
def create_todo(request):
    if request.method == 'POST':
        form = ToDoCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login_success'))
    else:
        form = ToDoCreateForm()
    return render(request, "create-todo.html", locals())


@login_required(login_url="")
def edit_todo(request, id=None):
    obj = ToDoDetails.objects.get(id=int(id))
    if request.method == 'POST':
        form = ToDoCreateForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('login_success'))
    else:
        form = ToDoCreateForm(instance=obj)
    # locals() passes all available variables to front end, you can access it directly
    return render(request, "create-todo.html", locals())