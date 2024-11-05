from django import forms
from core.models import Topic, Entry
from core.settings import core_settings


class TopicCreationForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["title"]


class EntryCreationForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ["text"]

    def clean(self):
        super(EntryCreationForm, self).clean()
        text = self.cleaned_data.get("text")
        if len(text) < core_settings.MIN_ENTRY_CHARACTERS:
            self._errors["text"] = self.error_class(
                ["Entry Should Contain a minimum of 1 characters"]
            )
        if len(text) > core_settings.MAX_ENTRY_CHARACTERS:
            self._errors["text"] = self.error_class(
                ["Try to fit your idea in less that 1000000 characters"]
            )

        return self.cleaned_data
