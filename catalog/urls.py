
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from catalog.views import IndexView, TopicListView, TopicCreateView, TopicUpdateView, TopicDeleteView, \
    RedactorDeleteView, \
    RedactorUpdateView, RedactorCreateView, RedactorListView, NewspaperListView, NewspaperCreateView, \
    NewspaperUpdateView, NewspaperDeleteView, RedactorDetailView, NewspaperDetailView, AfterRegisterView

app_name = "catalog"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("after_register/", AfterRegisterView.as_view(), name="after-register"),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("topics/create/", TopicCreateView.as_view(), name="topic-create"),
    path(
        "topics/<int:pk>/update/", TopicUpdateView.as_view(), name="topic-update",
    ),
    path(
        "topics/<int:pk>/delete/", TopicDeleteView.as_view(), name="topic-delete",
    ),

    path("redactors/", RedactorListView.as_view(), name="redactor-list"),
    path("redactors/create/", RedactorCreateView.as_view(), name="redactor-create"),
    path(
        "redactors/<int:pk>/detail/", RedactorDetailView.as_view(), name="redactor-detail",
    ),
    path(
        "redactors/<int:pk>/update/", RedactorUpdateView.as_view(), name="redactor-update",
    ),
    path(
        "redactors/<int:pk>/delete/", RedactorDeleteView.as_view(), name="redactor-delete",
    ),

    path("newspapers/", NewspaperListView.as_view(), name="newspaper-list"),
    path("newspapers/create/", NewspaperCreateView.as_view(), name="newspaper-create"),
    path(
        "newspapers/<int:pk>/detail/", NewspaperDetailView.as_view(), name="newspaper-detail",
    ),
    path(
        "newspapers/<int:pk>/update/", NewspaperUpdateView.as_view(), name="newspaper-update",
    ),
    path(
        "newspapers/<int:pk>/delete/", NewspaperDeleteView.as_view(), name="newspaper-delete",
    ),
]
