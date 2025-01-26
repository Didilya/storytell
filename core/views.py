import logging
import json
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic.base import View, TemplateResponseMixin
from core.utils.queries import (
    get_trending_topics,
    get_all_entries,
    get_topics_most_fav_entry,
    get_entry_by_uid,
    get_or_create_to_favorite,
    get_topics_entries,
    get_best_entries,
)
from core.serializers import TopicSerializer, EntrySerializer
from users.serializers import UserSerializer
from core.forms import TopicCreationForm, EntryCreationForm
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.paginator import Paginator

logger = logging.getLogger(__name__)


class MainPageView(TemplateResponseMixin, View):
    template_name = "main_page.html"

    def get(self, request, *args, **kwargs):
        top_topics = get_trending_topics()
        entries = get_all_entries()
        entries_data = EntrySerializer(entries, many=True).data
        top_topics_data = TopicSerializer(top_topics, many=True).data
        # logger.debug(f"entries_data={entries_data}, top_topics_data={top_topics_data}")
        context = {
            "user": request.user,
            "entries": entries_data,
            "top_topics": top_topics_data,
            "all_best_entries": get_topics_most_fav_entry(top_topics)[:25],
            "pagination_html": render_to_string(
                "pagination.html",
                {"page_data": {"page": 1, "topic": "all", "last_page": 5}},
            ),
        }
        if request.user.is_authenticated:
            context["user_data"] = UserSerializer(request.user).data
        return self.render_to_response(context)


class AddTopicView(TemplateResponseMixin, View):
    template_name = "add_topic.html"

    def get_context_data(self, **kwargs):
        context = {
            "topic_form": kwargs.get("topic_form", TopicCreationForm()),
            "entry_form": kwargs.get("entry_form", EntryCreationForm()),
        }
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        topic_form = TopicCreationForm(request.POST)
        entry_form = EntryCreationForm(request.POST)

        if not request.user.is_authenticated:
            messages.info(request, "You should Sign In to post topics and entries!")
            return redirect("login")

        if topic_form.is_valid() and entry_form.is_valid():
            topic = topic_form.save(commit=False)
            topic.user = request.user
            topic.save()
            entry = entry_form.save(commit=False)
            entry.topic = topic
            entry.user = request.user
            entry.save()
            return redirect("/")

        # If forms are not valid, render the page with validation errors
        context = self.get_context_data(topic_form=topic_form, entry_form=entry_form)
        return self.render_to_response(context)


class AddFavorite(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            data = {"error": "You should Sign In to add to favorites"}
            return JsonResponse(data, status=403)
        data = json.loads(request.body)
        entry_uid = data.get("entry")
        logger.debug(f"FAVORITE DATA {data}")
        entry = get_entry_by_uid(entry_uid)
        logger.debug(f"FAVORITE ENTRY {entry}")
        add_to_fav = get_or_create_to_favorite(request.user, entry)
        logger.debug(f"FAVORITE CREATED? {add_to_fav}")
        if not add_to_fav:
            data = {"error": "You already added this entry to favorites"}
            return JsonResponse(data, status=404)

        return redirect("/")


class TopicPopularEntries(TemplateResponseMixin, View):
    template_name = "entries_page.html"

    def get(self, request, uid, *args, **kwargs):
        best_entries = get_best_entries(uid)
        entries_data = EntrySerializer(best_entries, many=True).data
        top_topics = get_trending_topics()
        top_topics_data = TopicSerializer(top_topics, many=True).data
        # logger.debug(f"entries_data={entries_data}, top_topics_data={top_topics_data}")
        context = {
            "user": request.user,
            "top_topics": top_topics_data,
            "entries": entries_data,
            "pagination_html": render_to_string(
                "pagination.html",
                {"page_data": {"page": 1, "topic": uid, "last_page": 5}},
            ),
        }
        return self.render_to_response(context)


class TopicPageView(View):

    def get(self, request, uid, page_number=None, *args, **kwargs):
        if uid == "all":
            entries_data = get_topics_most_fav_entry(get_trending_topics())
            logger.debug(f"ALL case entries_data{entries_data}")
        else:
            entries = get_topics_entries(uid)
            entries_data = EntrySerializer(entries, many=True).data
            logger.debug(f"NOT ALL case entries_data{entries_data}")
        paginator = Paginator(entries_data, 25)
        page_obj = paginator.get_page(page_number)

        logger.debug(
            f"page_obj={page_obj}, page_number {page_number}, topic_uid={uid},entries={page_obj.object_list}"
        )
        return JsonResponse(
            {
                "entries": page_obj.object_list,
                "pagination_html": render_to_string(
                    "pagination.html",
                    {"page_data": {"page": page_number, "topic": uid, "last_page": 5}},
                ),
            },
            status=200,
        )
