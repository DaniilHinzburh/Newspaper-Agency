"""
URL configuration for newspaper_agency project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.newspaper_agency.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from catalog.views import IndexView, TopicListView, TopicCreateView, TopicUpdateView, TopicDeleteView, RedactorDeleteView, \
    RedactorUpdateView, RedactorCreateView, RedactorListView, NewspaperListView, NewspaperCreateView, \
    NewspaperUpdateView, NewspaperDeleteView, RedactorDetailView, NewspaperDetailView

app_name = "catalog"
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
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
