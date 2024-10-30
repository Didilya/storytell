from core.models import Topic, Entry, Favorite, Vote
from django.db.models import Count
import logging
from core.serializers import EntrySerializer

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

def get_all_entries():
    return Entry.objects.annotate(favorite_count=Count("favorites")).order_by(
        "-favorite_count"
    )

def get_topics_most_fav_topic(topic_ids):
    topics_fav_entry_list = []
    for id in topic_ids:
        topic = Topic.objects.get(id=id)
        queryset = Entry.objects.filter(topic=topic).all().annotate(favorite_count=Count("favorites")).order_by(
            "-favorite_count"
        )
        data = EntrySerializer(queryset, many=True, context={'title': topic.title}).data
        logger.debug(f"FAV ENTRIES={data}")
        topics_fav_entry_list.append(data)
    logger.debug(f"ALL FAV ENTRIES={topics_fav_entry_list}")
    return topics_fav_entry_list



def get_entries_count(topic):
    return Entry.objects.filter(topic=topic).count()
