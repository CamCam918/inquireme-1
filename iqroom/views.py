from django.shortcuts import render
from .forms import BlogCommentsForm


def showform(request):
    form = BlogCommentsForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'form': form}

    return render(request, 'Blog/tvreview.html', context)
