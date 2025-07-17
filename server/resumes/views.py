from resumes.models import Resume
from resumes.forms import ResumeForm
from django.shortcuts import render, redirect
from django.http import Http404
from django.shortcuts import redirect, get_object_or_404
from resumes.forms import ResumeURLFormSet

def resume_index(request):
    # Show list of resumes
    resumes = Resume.objects.all()
    return render(request, 'resume_index.html', {'resumes': resumes})

def resume_create(request):
    # Show form to create resume
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            resume = form.save()
            formset = ResumeURLFormSet(request.POST, instance=resume)
            if formset.is_valid():
                formset.save()
                return redirect('resume_detail', pk=resume.pk)
        else:
            formset = ResumeURLFormSet(request.POST)
    else:
        form = ResumeForm()
        formset = ResumeURLFormSet()
    return render(request, 'resume_create.html', {'form': form, 'formset': formset})

def resume_detail(request, pk):
    # Show a specific resume
    resume = get_object_or_404(Resume, pk=pk)
    urls = resume.urls.all()
    return render(request, 'resume_detail.html', {'resume': resume, 'urls': urls})

def resume_delete(request, pk):
    resume = get_object_or_404(Resume, pk=pk)
    if request.method == 'POST':
        resume.delete()
        return redirect('resume_index')
    return redirect('resume_detail', pk=pk)