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

from catalog.views import index, TopicListView, TopicCreateView, TopicUpdateView, TopicDeleteView

app_name = "catalog"
urlpatterns = [
    path("", index, name="index"),
    path("topics/", TopicListView.as_view(), name="topic-list"),
    path("topics/create/", TopicCreateView.as_view(), name="topic-create"),
    path(
        "topics/<int:pk>/update/", TopicUpdateView.as_view(), name="topic-update",
    ),
    path(
        "topics/<int:pk>/delete/", TopicDeleteView.as_view(), name="topic-delete",
    ),
]
