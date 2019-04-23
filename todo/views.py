from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import ToDoCreateForm

@login_required(login_url="")
def login_success(request):
    ct = {}
    ct['user'] = request.user
    return render(request, "todo-home.html", ct)

@login_required(login_url="")
def create_todo(request):
    if request.method == 'POST':
        form = ToDoCreateForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ToDoCreateForm()
    return render(request, "create-todo.html", locals())
