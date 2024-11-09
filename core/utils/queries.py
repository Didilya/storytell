from core.models import Topic, Entry, Favorite, Vote
from django.db.models import Count
import logging
from core.serializers import EntrySerializer
from django.shortcuts import get_object_or_404
import uuid

logger = logging.getLogger(__name__)


def get_topics_entries(topic_id):
    topic = Topic.objects.get(id=topic_id)
    return Entry.objects.filter(topic=topic).all()


def get_trending_topics():
    topics = Topic.objects.annotate(entry_count=Count("entries")).order_by(
        "-entry_count"
    )
    # logger.debug(f"TOPICS={topics} and {[e.entry_count for e in topics]}")
    return topics


def get_all_entries():
    return Entry.objects.annotate(favorite_count=Count("favorites")).order_by(
        "-favorite_count"
    )


def get_topics_most_fav_entry(topic_ids):
    topics_fav_entry_list = []
    for topic_id in topic_ids:
        topic = Topic.objects.get(id=topic_id)
        queryset = (
            Entry.objects.filter(topic=topic)
            .all()
            .annotate(favorite_count=Count("favorites"))
            .order_by("-favorite_count")
        )
        if not queryset:
            continue
        data = EntrySerializer(queryset, many=True, context={"title": topic.title}).data
        best_entry = data[0]
        topics_fav_entry_list.append(best_entry)
    # logger.debug(f"ALL FAV ENTRIES={topics_fav_entry_list}")
    return topics_fav_entry_list


def get_entries_count(topic):
    return Entry.objects.filter(topic=topic).count()


def get_entry_by_uid(uid_str):
    logger.debug(f"Before Extracted entry's uid={uid_str}")
    uid = uuid.UUID(uid_str)
    logger.debug(f"Extracted entry's uid={uid}")
    return Entry.objects.filter(uid=uid).first()  # get_object_or_404(Entry, uid=uid)


def get_or_create_to_favorite(user, entry):
    _, created_bool = Favorite.objects.get_or_create(user=user, entry=entry)
    return created_bool
