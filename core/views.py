import logging
from django.shortcuts import render
from django.views.generic.base import View, TemplateResponseMixin
from core.utils.queries import (
    get_topics_entries,
    get_trending_topics,
    get_all_entries,
    get_topics_most_fav_entry,
)
from core.serializers import TopicSerializer, EntrySerializer
from users.serializers import UserSerializer

logger = logging.getLogger(__name__)


class MainPageView(TemplateResponseMixin, View):
    template_name = "main_page.html"

    def get(self, request, *args, **kwargs):
        top_topics = get_trending_topics()
        top_topics_ids = top_topics.values_list("id", flat=True)
        entries = get_all_entries()
        entries_data = EntrySerializer(entries, many=True).data
        top_topics_data = TopicSerializer(top_topics, many=True).data
        logger.debug(f"entries_data={entries_data}, top_topics_data={top_topics_data}")
        context = {
            "user": request.user,
            "entries": entries_data,
            "top_topics": top_topics_data,
            "all_best_entries": get_topics_most_fav_entry(top_topics_ids),
        }
        if request.user.is_authenticated:
            context["user_data"] = UserSerializer(request.user).data
        logger.debug(f"ALL CONTEXT {context}")
        return self.render_to_response(context)


class AddTopicView(TemplateResponseMixin, View):
    template_name = "main_page.html"

    def get(self, request, *args, **kwargs):
        top_topics = get_trending_topics()
        top_topics_ids = top_topics.values_list("id", flat=True)
        entries = get_all_entries()
        entries_data = EntrySerializer(entries, many=True).data
        top_topics_data = TopicSerializer(top_topics, many=True).data
        logger.debug(f"entries_data={entries_data}, top_topics_data={top_topics_data}")
        context = {
            "entries": entries_data,
            "top_topics": top_topics_data,
            "all_best_entries": get_topics_most_fav_entry(top_topics_ids),
        }
        logger.debug(f"ALL CONTEXT {context}")
        return self.render_to_response(context)
