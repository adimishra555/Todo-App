from django.shortcuts import render,redirect,get_object_or_404
from .models import Todo

# Create your views here.
def index(request):
    todo=Todo.objects.all()
    if request.method=='POST':
        new_todo=Todo(
            title=request.POST['title']
        )
        new_todo.save()
        return redirect('/')

    return render(request,'index.html',{'todos':todo})

def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('/')

def update(request, pk):
    todo = get_object_or_404(Todo, id=pk)
    if request.method == 'POST':
        todo.title = request.POST.get('title')
        todo.save()
        return redirect('/')
    return render(request, 'index.html', {'todo': todo})


def remove_all(request):
    Todo.objects.all().delete()
    return redirect('/')



