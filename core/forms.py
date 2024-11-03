from django import forms
from core.models import Topic, Entry


class TopicCreationForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["user", "title"]


class EntryCreationForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ["user", "topic", "text"]
