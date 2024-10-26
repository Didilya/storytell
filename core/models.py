from django.db import models
from model_utils.models import TimeStampedModel


class Topic(TimeStampedModel):
    user = models.ForeignKey("users.User",
        on_delete=models.PROTECT,
        related_name="topics",)
    title = models.CharField("topic title", max_length=255)


class Entry(TimeStampedModel):
    user = models.ForeignKey("users.User",
        on_delete=models.PROTECT,
        related_name="entries",)
    text = models.TextField("text of the entry", blank=True, null=True)
    is_deleted = models.BooleanField(default=False)


class Favorite(models.Model):
    user = models.ForeignKey("users.User",
        on_delete=models.PROTECT,
        related_name="favorites",)
    entry = models.ForeignKey("Entry",
        on_delete=models.CASCADE,
        related_name="favorites",)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [('entry', 'user')]


class Vote(models.Model):
    user = models.ForeignKey("users.User",
        null=True,
        on_delete=models.PROTECT,
        related_name="votes",)
    entry = models.ForeignKey("Entry",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="votes",)
    is_good = models.BooleanField(default=False)
    is_bad = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

