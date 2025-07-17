from resumes.models import Resume
from resumes.forms import ResumeForm
from django.shortcuts import render, redirect
from django.http import Http404
from django.shortcuts import get_object_or_404

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
            return redirect('resume_detail', pk=resume.pk)
    else:
        form = ResumeForm()
    return render(request, 'resume_create.html', {'form': form})

def resume_detail(request, pk):
    # Show a specific resume
    resume = get_object_or_404(Resume, pk=pk)
    return render(request, 'resume_detail.html', {'resume': resume})