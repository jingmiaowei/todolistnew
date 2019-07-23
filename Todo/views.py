from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import Todolist
from django.http import  HttpResponseRedirect

# Create your views here.
def TodoListView(request):
    if request.method == 'POST':
        if request.POST['todo'] == '':
            content = {'all_items':Todolist.objects.all(), 'warn':'please add！'}
            return render(request, "home.html", content)
        else:
            a_row = Todolist(title=request.POST['todo'])
            a_row.save()
            content = {'all_items':Todolist.objects.all(), 'info':'add success！'}
            return render(request,"home.html", content)
    elif request.method == 'GET':
        content = {'all_items': Todolist.objects.all()}
        return render(request, "home.html" ,content)

def TodoAdd(request):
    new_todo = Todolist(content = request.POST['title'])
    new_todo.save()
    return render(request,"home.html", {'all_items': all_todo_items})

def TodoDelete(request,Todolist_id):
    delete_todo = Todolist.objects.get(id=Todolist_id)
    delete_todo.delete()
    success_url = reverse_lazy ('home')

def TodoEdit(request):
    return render(request,'edit.html') 
 
 
def NewEdit(request,Todolist_id):
    if request.method == 'POST':
        new_todo = Todolist(id=Todolist_id)
        new_todo.title = request.POST['edited']
        new_todo.save()
        return redirect('home')
    elif request.method == 'GET':
        content1 = {'needadd': Todolist.objects.get(id=Todolist_id).title }
        return render(request,'newedit.html',content1)  

def Finish(request, Todolist_id): 
    if request.POST['status'] == 'finished':
        a= Todolist.objects.get(id=Todolist_id)
        a.finish = True
        a.save()
        return redirect ('home')
    else:
        a = Todolist.objects.get(id=Todolist_id)
        a.finish = False
        a.save()
        return redirect ('home')
