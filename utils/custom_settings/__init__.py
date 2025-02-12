from django.conf import settings
from django.utils.module_loading import import_string


def perform_import(value, setting_name):
    if isinstance(value, str):
        return import_from_string(value, setting_name)
    elif isinstance(value, (list, tuple)):
        return [import_from_string(item, setting_name) for item in value]
    return value


def import_from_string(value, setting_name):
    try:
        return import_string(value)
    except ImportError as e:
        raise ImportError(
            f"Could not import '{value}' for setting '{setting_name}'. "
            f"{e.__class__.__name__}: {e}.",
        )


class ModuleSettings:
    def __init__(self, name, defaults=None, import_strings=None):
        self.name = name
        self.defaults = defaults or []
        self.import_strings = import_strings or []

    @property
    def user_settings(self):
        if not hasattr(self, "_user_settings"):
            self._user_settings = getattr(settings, self.name, {})
        return self._user_settings

    def __getattr__(self, attr):
        if attr not in self.defaults:
            raise AttributeError(f"Invalid setting: '{attr}'")

        value = self.user_settings.get(attr, self.defaults[attr])

        if attr in self.import_strings:
            value = perform_import(value, attr)

        setattr(self, attr, value)
        return value
