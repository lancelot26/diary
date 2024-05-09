from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required

def forum(request):
    notes = Note.objects.all()
    return render(request, 'main/forum.html', {'notes':notes})

@login_required(login_url='/users/login/')
def diary(request):
    notes = Note.objects.all()
    return render(request, 'main/diary.html', {'notes':notes})

@login_required(login_url='/users/login/')
def create_note(request):
    error=''
    if request.method == 'POST':
        form = NoteForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('diary_list')
        else:
            error = 'error'
    form = NoteForm()
    data = {
        'form':form,
        'error':error
    }
    return render(request, 'main/create_post.html', data)

class ViewNote(DeleteView):
    model = Note
    template_name = 'main/view_note.html'
    context_object_name = 'view_note'


class UpdateNote(UpdateView):
    model = Note
    template_name = 'main/create_post.html'
    form_class = NoteForm


class DeleteNote(DeleteView):
    model = Note
    success_url = '/'
    template_name = 'main/delete_note.html'