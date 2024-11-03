from django.urls import path
from . import views

urlpatterns = [
    path("", views.MainPageView.as_view(), name="top_entries"),
    path("exorcise/", views.AddTopicView.as_view(), name="new_topic")
]
