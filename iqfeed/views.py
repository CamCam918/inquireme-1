from django.shortcuts import render
from .forms import PostModelForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)


class IqCreateView(LoginRequiredMixin, CreateView):
    model = PostModelForm
    template_name = "news_new.html"
    fields = ["title", "body", "picture"]


def showform(request):
    form = PostModelForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {'form': form}

    return render(request, '/feed.html', context)
