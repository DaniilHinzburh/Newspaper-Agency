from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import NewspaperForm
from .models import Redactor, Topic, Newspaper


def index(request):
    return render(request, "catalog/index.html")


class TopicListView(LoginRequiredMixin, generic.ListView):
    model = Topic
    context_object_name = "topic_list"
    template_name = "catalog/topic_list.html"
    paginate_by = 5


class TopicCreateView(LoginRequiredMixin, generic.CreateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("catalog:topic-list")
    template_name = "catalog/topic_form.html"


class TopicUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Topic
    fields = "__all__"
    success_url = reverse_lazy("catalog:topic-list")


class TopicDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Topic
    success_url = reverse_lazy("catalog:topic-list")
    template_name = "catalog/topic_delete_form.html"


class RedactorListView(LoginRequiredMixin, generic.ListView):
    model = Redactor
    context_object_name = "redactor_list"
    template_name = "catalog/redactor_list.html"
    paginate_by = 5


class RedactorDetailView(LoginRequiredMixin, generic.DetailView):
    model = Redactor
    queryset = Redactor.objects.all().prefetch_related("newspaper_set__topics")


class RedactorCreateView(LoginRequiredMixin, generic.CreateView):
    model = Redactor
    fields = "__all__"
    success_url = reverse_lazy("catalog:redactor-list")
    template_name = "catalog/redactor_form.html"


class RedactorUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Redactor
    fields = "__all__"
    success_url = reverse_lazy("catalog:redactor-list")


class RedactorDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Redactor
    success_url = reverse_lazy("catalog:redactor-list")
    template_name = "catalog/redactor_delete_form.html"


class NewspaperListView(LoginRequiredMixin, generic.ListView):
    model = Newspaper
    context_object_name = "newspaper_list"
    template_name = "catalog/newspaper_list.html"
    paginate_by = 5


class NewspaperDetailView(LoginRequiredMixin, generic.DetailView):
    model = Newspaper


class NewspaperCreateView(LoginRequiredMixin, generic.CreateView):
    model = Newspaper
    form_class = NewspaperForm

    success_url = reverse_lazy("catalog:newspaper-list")
    template_name = "catalog/newspaper_form.html"


class NewspaperUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Newspaper
    fields = "__all__"
    success_url = reverse_lazy("catalog:newspaper-list")


class NewspaperDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Newspaper
    success_url = reverse_lazy("catalog:newspaper-list")
    template_name = "catalog/newspaper_delete_form.html"
