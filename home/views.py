from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo, Person
from django.contrib import messages
from .forms import TodoForm , UpgradeTodoForm

# Create your views here.
def home(request):
    all = Todo.objects.all()
    return render(request, 'home.html', {'all':all})

def sajjad(request):
    users = Person.objects.all()
    return render(request, 'sajjad.html', {"Users":users} )

def detail(request, todo_id):
    todo = Todo.objects.get(id = todo_id)
    return render(request , 'detail.html', {'todo':todo})

def delete(request, todo_id):
    Todo.objects.get(id = todo_id).delete()
    messages.success(request, 'delete success', extra_tags='danger' )
    return redirect('home')

def pdetail(request, pd):
    user = Person.objects.get(id=pd)
    return render(request, 'person_detail.html', {'user':user})

def pdelete(request, pd):
    Person.objects.get(id = pd).delete()
    return redirect('sajjad')

def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(title = cd['title'], body = cd['body'], created = cd['created'])
            messages.success(request,'added todo', extra_tags='warning')
            return redirect('home')
        
    else:
        form = TodoForm()
    return render(request, 'create.html', {'form':form})

def update(request,todo_id):
    todo = Todo.objects.get(id = todo_id)
    if request.method == 'POST':
        form = UpgradeTodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request,'todo updated', 'success')
            return redirect('detail', todo_id)
    else:
        form = UpgradeTodoForm(instance=todo)
        return render(request, 'update.html', {'form':form})
