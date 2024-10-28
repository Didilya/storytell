from django.db import models
from model_utils.models import TimeStampedModel


class Topic(TimeStampedModel):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.PROTECT,
        related_name="topics",
    )
    title = models.CharField("topic title", max_length=255)

    def __str__(self):
        return self.title


class Entry(TimeStampedModel):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.PROTECT,
        related_name="entries",
    )
    topic = models.ForeignKey(
        "Topic",
        on_delete=models.CASCADE,
        related_name="entries",
        null=True,
    )
    text = models.TextField("text of the entry", blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text[:40]}..."


class Favorite(models.Model):
    user = models.ForeignKey(
        "users.User",
        on_delete=models.PROTECT,
        related_name="favorites",
    )
    entry = models.ForeignKey(
        "Entry",
        on_delete=models.CASCADE,
        related_name="favorites",
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = [("entry", "user")]

    def __str__(self):
        return f"{self.entry.text[:40]}..."


class Vote(models.Model):
    user = models.ForeignKey(
        "users.User",
        null=True,
        on_delete=models.PROTECT,
        related_name="votes",
    )
    entry = models.ForeignKey(
        "Entry",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="votes",
    )
    is_good = models.BooleanField(default=False)
    is_bad = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.entry.text[:40]}... is_good {self.is_good} is_bad {self.is_bad}"
