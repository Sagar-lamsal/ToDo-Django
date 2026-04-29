from django.shortcuts import render , redirect
from .models import task
from .forms import taskinput

# Create your views here.
def home(request):
    tasks = task.objects.all()
    form = taskinput()

    if request.method =='POST':
        if 'delete' in request.POST:
            task_id = request.POST.get('task_id')
            task.objects.get(id=task_id).delete()   
            return redirect('home')
        
        elif 'edit' in request.POST :
            task_id = request.POST.get('task_id')
            task_obj = task.objects.get(id=task_id)
            form = taskinput(instance=task_obj)

        elif 'add_task' or 'update_task' in request.POST:
            task_id = request.POST.get('task_id')
            if task_id:
                task_obj = task.objects.get(id=task_id)
                form = taskinput(request.POST , instance=task_obj)
            else:
                form = taskinput(request.POST)

            if form.is_valid():
                form.save()
                return redirect('home')

    context = {
        'tasks' :tasks,
        'form' :form
    }
    return render(request , 'home.html', context)