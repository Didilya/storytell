from django.shortcuts import render
from django.views.generic.base import View, TemplateResponseMixin
from core.utils import get_topics_entries, get_trending_topics

class MainPageView(TemplateResponseMixin, View):
    template_name = 'main_page.html'

    def get_todays_trending_data(self):
        return get_trending_topics()

    def get(self, request, *args, **kwargs):
        context = self.get_todays_trending_data()
        return self.render_to_response(request, context)

def top_entries(request):
    context = {
        "entries": [
            {
                "title": "Some very interesting entry",
                "content": "This is the content of the first example entry.Let's check how big content can be if I will continue typing how many types I can type?",
                "user": "Diuser1",
                "save_count": 6,
                "thumbnail": "users/users_thumbnails/dilyara_diyarova1.jpg",
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
            },
            # Add more entries as needed
        ],
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
