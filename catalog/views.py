from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Redactor, Topic, Newspaper


def index(request):
    return render(request, "catalog/index.html")


class TopicListView(generic.ListView):
    model = Topic
    context_object_name = "topic_list"
    template_name = "catalog/topic_list.html"
    paginate_by = 5


class TopicCreateView(generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("catalog:topic-list")
    template_name = "catalog/topic_form.html"


class TopicUpdateView(generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("catalog:topic-list")


class TopicDeleteView(generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("catalog:topic-list")
    template_name = "catalog/topic_delete_form.html"


class RedactorListView(generic.ListView):
    model = Redactor
    context_object_name = "redactor_list"
    template_name = "catalog/redactor_list.html"
    paginate_by = 5


class RedactorCreateView(generic.CreateView):
    model = Redactor
    fields = "__all__"
    success_url = reverse_lazy("catalog:redactor-list")
    template_name = "catalog/redactor_form.html"


class RedactorUpdateView(generic.UpdateView):
    model = Redactor
    fields = "__all__"
    success_url = reverse_lazy("catalog:redactor-list")


class RedactorDeleteView(generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("catalog:redactor-list")
    template_name = "catalog/redactor_delete_form.html"



class NewspaperListView(generic.ListView):
    model = Newspaper
    context_object_name = "newspaper_list"
    template_name = "catalog/newspaper_list.html"
    paginate_by = 5


class NewspaperCreateView(generic.CreateView):
    model = Newspaper
    fields = "__all__"
    success_url = reverse_lazy("catalog:newspaper-list")
    template_name = "catalog/newspaper_form.html"


class NewspaperUpdateView(generic.UpdateView):
    model = Newspaper
    fields = "__all__"
    success_url = reverse_lazy("catalog:newspaper-list")


class NewspaperDeleteView(generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("catalog:newspaper-list")
    template_name = "catalog/newspaper_delete_form.html"