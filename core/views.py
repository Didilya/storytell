import logging
from django.shortcuts import render
from django.views.generic.base import View, TemplateResponseMixin
from core.utils.queries import (
    get_topics_entries,
    get_trending_topics,
    get_all_entries,
    get_topics_most_fav_topic,
)
from core.serializers import TopicSerializer, EntrySerializer

logger = logging.getLogger(__name__)


test_entries = [
    {
        "title": "Some very interesting entry",
        "content": "This is the content of the first example entry.Let's check how big content can be if I will continue typing how many types I can type?",
        "user": "Diuser1",
        "save_count": 6,
        "thumbnail": "users/users_thumbnails/Screen_Shot_2022-12-08_at_03.55.36.png",
    },
    {
        "title": "not so interesting entry",
        "content": "Here is some more example content for another entry.",
        "user": "Touser2",
        "save_count": 7,
        "thumbnail": "users/users_thumbnails/tolga_topcu1.jpg",
    },
    {
        "title": "even less interesting entry",
        "content": "Here is some more example content for another entry.",
        "user": "user3",
        "save_count": 10,
        "thumbnail": "users/users_thumbnails/dilyara_diyarova1.jpg",
    },
]

# context= {
# "all_best_entries": [{'user': {'profile_name': 'DidiUser', 'email': 'didi1111@mail.com', 'thumbnail': 'users/users_thumbnails/story_points.png'}, 'topic': 4, 'text': "I'm little bit an insecure", 'created': '2024-10-29T15:00:21.083475Z', 'favorite_count': 0, 'title': 'Very stupid topic'},
# }


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
            "entries": entries_data,
            "top_topics": top_topics_data,
            "all_best_entries": get_topics_most_fav_topic(top_topics_ids),
        }
        logger.debug(f"ALL CONTEXT {context}")
        return self.render_to_response(context)


def top_entries(request):
    context = {
        "entries": test_entries,
        "top_topics": [
            {
                "title": "Some topic that longer that others so it will need more spase into the spase of Technology",
                "url": "#",
                "entry_count": 42,
            },
            {"title": "Latest in Science", "url": "#", "entry_count": 35},
            {"title": "Health and Wellness", "url": "#", "entry_count": 28},
            {"title": "Economics Today", "url": "#", "entry_count": 20},
            {"title": "Entertainment Highlights", "url": "#", "entry_count": 15},
            {"title": "Trending in Technology", "url": "#", "entry_count": 42},
            {"title": "Latest in Science", "url": "#", "entry_count": 35},
            {"title": "Health and Wellness", "url": "#", "entry_count": 28},
            {"title": "Economics Today", "url": "#", "entry_count": 20},
            {"title": "Entertainment Highlights", "url": "#", "entry_count": 15},
            {"title": "Trending in Technology", "url": "#", "entry_count": 42},
            {"title": "Latest in Science", "url": "#", "entry_count": 35},
            {"title": "Health and Wellness", "url": "#", "entry_count": 28},
            {"title": "Economics Today", "url": "#", "entry_count": 20},
            {"title": "Entertainment Highlights", "url": "#", "entry_count": 15},
            {"title": "Trending in Technology", "url": "#", "entry_count": 42},
            {"title": "Latest in Science", "url": "#", "entry_count": 35},
            {"title": "Health and Wellness", "url": "#", "entry_count": 28},
            {"title": "Economics Today", "url": "#", "entry_count": 20},
            {"title": "Entertainment Highlights", "url": "#", "entry_count": 15},
            {"title": "Trending in Technology", "url": "#", "entry_count": 42},
            {"title": "Latest in Science", "url": "#", "entry_count": 35},
            {"title": "Health and Wellness", "url": "#", "entry_count": 28},
            {"title": "Economics Today", "url": "#", "entry_count": 20},
            {"title": "Entertainment Highlights", "url": "#", "entry_count": 15},
            {"title": "Trending in Technology", "url": "#", "entry_count": 42},
            {"title": "Latest in Science", "url": "#", "entry_count": 35},
            {"title": "Health and Wellness", "url": "#", "entry_count": 28},
            {"title": "Economics Today", "url": "#", "entry_count": 20},
            {"title": "Entertainment Highlights", "url": "#", "entry_count": 15},
            {"title": "Trending in Technology", "url": "#", "entry_count": 42},
            {"title": "Latest in Science", "url": "#", "entry_count": 35},
            {"title": "Health and Wellness", "url": "#", "entry_count": 28},
            {"title": "Economics Today", "url": "#", "entry_count": 20},
            {"title": "Entertainment Highlights", "url": "#", "entry_count": 15},
            {"title": "Trending in Technology", "url": "#", "entry_count": 42},
            {"title": "Latest in Science", "url": "#", "entry_count": 35},
            {"title": "Health and Wellness", "url": "#", "entry_count": 28},
            {"title": "Economics Today", "url": "#", "entry_count": 20},
            {"title": "Entertainment Highlights", "url": "#", "entry_count": 15},
            # Add more topics as needed
        ],
    }
    return render(request, "main_page.html", context)
