from core.models import Topic, Entry, Favorite, Vote
from django.db.models import Count

def get_topics_entries(topic_id):
    topic = Topic.objects.get(id=topic_id)
    return Entry.objects.filter(topic=topic).all()

def get_trending_topics():
    return Topic.objects.annotate(num_entries=Count("entry")).order_by("-num_entries")

def get_entries_count(topic):
    return Entry.objects.filter(topic=topic).count()