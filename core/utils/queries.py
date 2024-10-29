from core.models import Topic, Entry, Favorite, Vote
from django.db.models import Count
import logging

logger = logging.getLogger(__name__)


def get_topics_entries(topic_id):
    topic = Topic.objects.get(id=topic_id)
    return Entry.objects.filter(topic=topic).all()


def get_trending_topics():
    topics = Topic.objects.annotate(entry_count=Count("entries")).order_by(
        "-entry_count"
    )
    logger.debug(f"TOPICS={topics} and {[e.entry_count for e in topics]}")
    return topics


def get_entries_count(topic):
    return Entry.objects.filter(topic=topic).count()
