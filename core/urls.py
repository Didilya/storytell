from django.urls import path
from . import views

urlpatterns = [
    path("", views.MainPageView.as_view(), name="top_entries"),
    path("exorcise/", views.AddTopicView.as_view(), name="new_topic"),
    path("add_favorite/", views.AddFavorite.as_view(), name="add_favorite"),
    path(
        "topics/<str:uid>/<int:page_number>/",
        views.TopicPageView.as_view(),
        name="topic",
    ),
    path(
        "topics/<str:uid>/",
        views.TopicPopularEntries.as_view(),
        name="popular_entries",
    ),
]
