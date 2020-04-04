from django.shortcuts import render, redirect,get_object_or_404
from .models import Note
from .forms import NoteForm

def home(request):
    qs =  Note.objects.all()
    context = {
        "query":qs
    }
    return render(request, "notepad/home.html", context)

def create(request):
    title = 'create'
    form = NoteForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.instance.user = request.user
        form.save()
        return redirect('/')
    context = {
        "form":form,
        "title":title
    }
    return render(request, "notepad/create.html", context)
    
def update(request, id):
    title = 'update'
    qs = get_object_or_404(Note, id=id)
    form = NoteForm(request.POST or None, request.FILES or None, instance=qs)
    if request.method == "POST":
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('/')
       
    context = {
        "form":form,
        "title":title
    }
    return render(request, "notepad/create.html",context)
def delete(request,id):
    # my method
    # qs = get_object_or_404(Note,id=id)
    # qs.delete()
    # return redirect('/')

    # to avoid another user deleting an object, it has t be the main user

    qs = Note.objects.filter(id=id)
    if qs.exists():
        if request.user ==  qs[0].user:
            qs.delete()
    return redirect('/')