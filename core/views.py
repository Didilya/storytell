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
)
from core.serializers import TopicSerializer, EntrySerializer
from users.serializers import UserSerializer
from core.forms import TopicCreationForm, EntryCreationForm
from django.http import JsonResponse
from django.core import exceptions
from django.core.paginator import Paginator

logger = logging.getLogger(__name__)


class MainPageView(TemplateResponseMixin, View):
    template_name = "main_page.html"

    def get(self, request, *args, **kwargs):
        top_topics = get_trending_topics()
        top_topics_ids = top_topics.values_list("id", flat=True)
        entries = get_all_entries()
        entries_data = EntrySerializer(entries, many=True).data
        top_topics_data = TopicSerializer(top_topics, many=True).data
        # logger.debug(f"entries_data={entries_data}, top_topics_data={top_topics_data}")
        context = {
            "user": request.user,
            "entries": entries_data,
            "top_topics": top_topics_data,
            "all_best_entries": get_topics_most_fav_entry(top_topics_ids),
        }
        if request.user.is_authenticated:
            context["user_data"] = UserSerializer(request.user).data
        return self.render_to_response(context)


class AddTopicView(TemplateResponseMixin, View):
    template_name = "add_topic.html"
    context = {
        "topic_form": TopicCreationForm(),
        "entry_form": EntryCreationForm(),
    }

    def get(self, request, *args, **kwargs):
        context = {
            "topic_form": TopicCreationForm(),
            "entry_form": EntryCreationForm(),
        }
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        topic_form = TopicCreationForm(request.POST)
        entry_form = EntryCreationForm(request.POST)

        if not request.user.is_authenticated:
            messages.add_message(
                request, messages.INFO, "You should Sign In to post topics and entries!"
            )
            return self.render_to_response(self.context)

        if topic_form.is_valid() and entry_form.is_valid():
            topic = topic_form.save(commit=False)
            topic.user = request.user
            topic.save()
            entry = entry_form.save(commit=False)
            entry.topic = topic
            entry.user = request.user
            entry.save()

            return redirect("/")
        else:
            self.render_to_response(self.context)

        context = {
            "topic_form": topic_form,
            "entry_form": entry_form,
        }
        return self.render_to_response(context)


class AddFavorite(View):
    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            data = {"error": "You should Sign In to add to favorites"}
            return JsonResponse(
                data, status=403
            )  # or raise exceptions.PermissionDenied
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


class TopicPageView(TemplateResponseMixin, View):
    template_name = "topic_page.html"

    def get(self, request, uid, *args, **kwargs):
        entries = get_topics_entries(uid)
        entries_data = EntrySerializer(entries, many=True).data
        paginator = Paginator(entries_data, 25)
        logger.debug(
            f"entries_data={entries_data}, topic_uid={request.get('topic_uid')}. paginator={paginator}"
        )
        page_obj = paginator.get_page(request.get("page_number"))
        logger.debug(f"page_obj={page_obj}, request {request.get('page_number')}")
        top_topics = get_trending_topics()
        top_topics_data = TopicSerializer(top_topics, many=True).data
        context = {
            "top_topics": top_topics_data,
            "entries": entries_data,
        }
        return self.render_to_response(context)
